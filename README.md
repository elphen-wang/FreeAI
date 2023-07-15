# FreeAI
OpenAI should not be a closed AI. 

你是否还在为OpenAI需要科学上网在犯愁？

你是否还在为OpenAI的付费模式而望而却步？

你是否苦恼没有免费的API Key来开发自己的ChatGPT工具？

本项目综述Github众优秀开发者的努力，给出一个比较完美的解决方案，并持续向更好用更强大更便宜的AI开放努力。

**鸣谢：**
+ [pengzhile/pandora](https://github.com/pengzhile/pandora)：让OpenAI GPT-3.5的API免费和免科学上网的关键技术。
+ [acheong08/OpenAIAuth](https://github.com/acheong08/OpenAIAuth)：免科学上网获取自己OpenAI账户的Cookie。
+ [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic), 以它为例，解决它需翻墙和需要付费的OpenAI API key的问题，演示OpenAI变为FreeAI。

## Pandora
旨在打造免科学上网情况下，最原汁原味的ChatGPT。基于 的[技术原理](https://zhile.io/2023/05/19/how-to-get-chatgpt-access-token-via-pkce.html)实现的。目前有官方的体验网站[https://chat.zhile.io](https://chat.zhile.io)，需要使用OpenAI的账户密码，所有对话记录与在官网的一致；也有基于Pandora技术的共享[Shared Chat](https://baipiao.io/chatgpt)的资源池，无需账号密码也能体验。

Pandora项目最难能可贵的是提供了可将用户的Cookie转化为形式如同API key的Access Token和响应这个Access Token的反代接口（也可响应OpenAI原生接口）的服务，此举无疑是基于OpenAI自由开发者最大的福音。详情请见：[“这个服务旨在模拟 Turbo API，免费且使用的是ChatGPT的8k模型”](https://github.com/pengzhile/pandora/issues/837)。
+ Cookie转 `fk-`开头、43位的 Share Token 演示地址：[https://ai.fakeopen.com/token](https://ai.fakeopen.com/token)；
+ Cookie转 `pk-`开头、43位的 Pool Token 演示地址：[https://ai.fakeopen.com/pool](https://ai.fakeopen.com/pool)。解决多账号并发的问题；
+ 响应上述 Access Token 的反代接口是：[https://ai.fakeopen.com/v1/chat/completions](https://ai.fakeopen.com/v1/chat/completions)。

Pandora项目还提供了两个免费的Pool Token:
+ `pk-this-is-a-real-free-pool-token-for-everyone` 很多 Share Token 组成的池子。
+ `pk-this-is-a-real-free-api-key-pk-for-everyone` 一些120刀 Api Key组成的池子。`（我测试的时候已经没钱了，衰。）`
经使用自己的账号生成的Share Token和Pool Token进行测试，使用Access Token进行的对话的记录，不会出现在该账户记录中。所以我自己使用的也是Pandora提供Pool Token，毕竟自己的池子不够大，而且因为自己的用户cookie的生命周期只有14天，时常更新Access Token也很烦。

本人十分中意ChatGPT的翻译效果，所以编写一个基于Pandora的简易翻译服务的网页，即文件[Translate.html](https://github.com/elphen-wang/FreeAI/blob/main/Translate.html)进行测试，效果还可以。

## OpenAIAuth
如果，你在使用Pandora提供的Pool Token还有隐私和安全的顾虑，也可以同时使用[OpenAIAuth](https://github.com/acheong08/OpenAIAuth)和`pandora-chatgpt`的python函数包来产生和定时更新专属自己Access token。

Pandora项目也提供了[这种服务](https://gist.github.com/pengzhile/448bfcfd548b3ae4e665a84cc86c4694)。但是我实操后，还是觉得结合OpenAIAuth更好使一些，并把修改后的代码放进[get_freeai_api.py]()文件。
