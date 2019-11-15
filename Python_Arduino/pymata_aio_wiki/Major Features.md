# Major Features（主要特点）
+ 使用高效的Python [asyncio](https://docs.python.org/3/library/asyncio.html)库实现。
+ 从3个随附的API中选择
  + **pymata_core**——一个纯异步方法调用API。
  + **pymata3**——一个pymata_aio插件，实现了作为pymata_core的代理的方法调用API。它将用户从asyncio库的详细信息中屏蔽出来。
  + **pymata_iot**——一个pymata_aio插件API，它实现Websocket服务器，并使用JSON消息进行应用程序通信。
    + 下载并调用**pymata_iot**之后，[从网页控制Arduino！](http://mryslab.github.io/pymata-aio/examples/uno_iot_tester.html)
+ 实现100％的StandardFirmata协议（StandardFirmata 2.43）。
+ 自动检测Arduino COM端口。
+ 提供集成的Control-C处理程序。
+ 分发中包括FirmataPlus（增强的StandaradFirmata草图）。 它增加了对以下内容的支持：
  + HC-SRO4超声波距离传感器使用单个引脚。
  + 步进电机。
  + 压电音调生成。
  + 2针旋转编码器支持。
+ 能够基于每个引脚自动捕获用户指定的模拟和数字瞬态输入事件并为其加上时间戳。
+ 所有3个API均支持回调以及轮询接口。