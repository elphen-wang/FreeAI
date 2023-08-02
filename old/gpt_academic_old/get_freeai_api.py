# -*- coding: utf-8 -*-

from os import path
import requests
from OpenAIAuth import Auth0

def run():
    expires_in = 0
    unique_name = 'my share token'
    current_dir = path.dirname(path.abspath(__file__))
    credentials_file = path.join(current_dir, 'credentials.txt')
    share_tokens_file = path.join(current_dir, 'share_tokens.txt')
    with open(credentials_file, 'r', encoding='utf-8') as f:
        credentials = f.read().split('\n')
    credentials = [credential.split(',', 1) for credential in credentials]
    count = 0
    token_keys = []
    for credential in credentials:
        progress = '{}/{}'.format(credentials.index(credential) + 1, len(credentials))
        if not credential or len(credential) != 2:
            continue

        count += 1
        username, password = credential[0].strip(), credential[1].strip()
        token_info = {
            'token': 'None',
            'share_token': 'None',
        }
        token_keys.append(token_info)
        try:
            auth = Auth0(email=username, password=password)
            token_info['token'] = auth.get_access_token()
            #print('Login success: {}, {}'.format(username, progress))
        except Exception as e:
            err_str = str(e).replace('\n', '').replace('\r', '').strip()
            #print('Login failed: {}, {}'.format(username, err_str))
            token_info['token'] = err_str
            continue
        data = {
            'unique_name': unique_name,
            'access_token': token_info['token'],
            'expires_in': expires_in,
        }
        resp = requests.post('https://ai.fakeopen.com/token/register', data=data)
        if resp.status_code == 200:
            token_info['share_token'] = resp.json()['token_key']
        else:
            continue
    
    with open(share_tokens_file, 'w', encoding='utf-8') as f:
    # 如果账号大于一个，优先使用pool；只有一个时，使用单独的api；没有，则有公共pool。
        if count==0:
            f.write('pk-this-is-a-real-free-pool-token-for-everyone\n')
            f.write('pk-this-is-a-real-free-api-key-pk-for-everyone\n')
        elif count==1:
            f.write('{}\n'.format(token_keys[0]['share_token']))
        else:
            data = {
                'share_tokens': '\n'.join([token_info['share_token'] for token_info in token_keys]),
            }
            resp = requests.post('https://ai.fakeopen.com/pool/update', data=data)
            if resp.status_code == 200:
                f.write('{}\n'.format(resp.json()['pool_token']))
            for token_info in token_keys:
                f.write('{}\n'.format(token_info['share_token']))
    f.close()

if __name__ == '__main__':
    run()

