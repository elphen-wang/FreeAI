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
旨在打造免科学上网情况下，最原汁原味的ChatGPT。基于 Access Token 的[技术原理](https://zhile.io/2023/05/19/how-to-get-chatgpt-access-token-via-pkce.html)实现的。目前有官方的体验网站[https://chat.zhile.io](https://chat.zhile.io)，需要使用OpenAI的账户密码，所有对话记录与在官网的一致；也有基于Pandora技术的共享[Shared Chat](https://baipiao.io/chatgpt)的资源池，无需账号密码也能体验。

Pandora项目最难能可贵的是提供了可将Access Token转化为API key和响应这个API key的接口（也可响应OpenAI原生接口）的服务，此举无疑是基于OpenAI自由开发者最大的福音。详情请见：[“这个服务旨在模拟 Turbo API，免费且使用的是ChatGPT的8k模型”](https://github.com/pengzhile/pandora/issues/837)。
+ Access Token 转 `fk-`开头、43位的 API key演示地址：[https://ai.fakeopen.com/token](https://ai.fakeopen.com/token)；
+ Access Token 转 `pk-`开头、43位的Pool API key演示地址：[https://ai.fakeopen.com/pool](https://ai.fakeopen.com/pool)。解决多账号并发的问题；
+ 响应上述API key的反代接口是：[https://ai.fakeopen.com/v1/chat/completions](https://ai.fakeopen.com/v1/chat/completions)。

Pandora项目还提供了两个免费的Pool API key:
+ `pk-this-is-a-real-free-pool-token-for-everyone` 很多 Share Token 组成的池子。
+ `pk-this-is-a-real-free-api-key-pk-for-everyone` 一些120刀 Api Key组成的池子。`（我测试的时候已经没钱了，衰。）`
经使用自己的账号生成的Pool API key和API Key测试，使用API进行的对话的记录，不会出现在该账户记录中。所以我自己使用的也是Pandora提供Pool API key，毕竟自己的池子不够大。

基于此，我编写一个基于Pandora的简易翻译服务的网页，即文件``，测试效果还可以（本人十分中意ChatGPT的翻译效果）。

