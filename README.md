# FreeAI
OpenAI should not be a closed AI. 

你是否还在为OpenAI需要科学上网在犯愁？

你是否还在为OpenAI的付费模式而望而却步？

你是否苦恼没有免费的API Key来开发自己的ChatGPT工具？

本项目综述Github众优秀开发者的努力，给出一个比较完美的解决方案，并持续向更好用、更强大、更便宜的AI开放努力。**如果你喜欢本项目，请给一个免费的star，谢谢！**

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

本人十分中意ChatGPT的翻译效果，所以编写一个基于Pandora的简易翻译服务的网页，即文件[Translate.html](https://github.com/elphen-wang/FreeAI/blob/main/Translate.html)，测试效果表明还可以。

## OpenAIAuth
现在，Pandora的讨论帖就有人在提Access token想保留问询记录的需求。如果，你在使用Pandora提供的Pool Token还有隐私和安全的顾虑，也可以同时使用[OpenAIAuth](https://github.com/acheong08/OpenAIAuth)和`pandora-chatgpt`的python函数包来产生和定时更新专属自己Access token。

Pandora项目其实也独立提供了[这种服务](https://gist.github.com/pengzhile/448bfcfd548b3ae4e665a84cc86c4694)。但是我实操后，还是觉得结合OpenAIAuth更好使一些，并把修改后的代码放进[get_freeai_api.py](https://github.com/elphen-wang/FreeAI/blob/main/get_freeai_api.py)文件，生成的'share_tokens.txt'是Pool Token（如果有二个及以上的账户密码的话）和Share Token并在的。

## gpt_academic
本人之前搭建专属自己的OpenAI API反向代理的教程[ChatGPT Wallfree](https://github.com/elphen-wang/chatgpt_wallfree)只实现了gpt_academic免科学上网功能，但仍需使用OpenAI原生的API key。这里还是以它为例，本次直接不用开发者自己搭建反向代理服务和OpenAI原生的API key，可以为一般的科研组省下一笔的不易报销的经费支出。

开发者可使用本项目中[gpt_academic](https://github.com/elphen-wang/FreeAI/tree/main/gpt_academic)文件夹中文件替代官方的文件（`主要是修改对toolbox.py和和config_private.py对access token的识别和获取`），也可在此基础上加入自己的设定（如gpt_academic账户密码等）。如此之后，安装官方的调试运行和部署指引，gpt_academic就可以不用科学上网又能免费使用gpt-3.5啦！

在使用自己的账户的access token的场景中，需要用户自己设定定时执行get_freeai_api.py的功能，如每天凌晨四点执行一次。这样可以克服OpenAI cookie只有14天生命周期引入的频繁手动更新access token的问题。

`tips：由于gpt_academic设定用户参数配置的读取优先级: 环境变量 > config_private.py > config.py，所以调试中，最好config.py文件也做对应的修改。不然，用户的配置可能在某调试情况下不生效，这可能是gpt_academic的bug。`

## 后记
+ 因为，Pandora目前本质上是将OpenAI原生的网页服务还原出来，所以目前还不能免费使用诸如ChatGPT-4等付费内容。不过，这将是本人和一众致力于使AI技术服务更广大群众的开发者今后努力的方向。
+ 之前ChatGPT Wallfree教程中提及ZeroTier的内网穿透技术，实测不如[Frp](https://github.com/fatedier/frp)更适合中国宝宝的体质：更稳定、速度更快且第三方无需客户端。

## Star历史

![Star History Chart](https://api.star-history.com/svg?repos=elphen-wang/FreeAI&type=Date)


