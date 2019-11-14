# Home
![pymata_aio](https://camo.githubusercontent.com/026940cd9bfe4ebb86d014da5ecfdf9099729bba/68747470733a2f2f7261772e6769746875622e636f6d2f4d7259734c61622f70796d6174612d61696f2f6d61737465722f646f63756d656e746174696f6e2f696d616765732f6c6f676f2e706e67)  
## 重要说明：
如果要升级到版本2.22并使用FirmataPlus，请同时[升级您的FirmataPlus版本](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-FirmataPlus-to-Arduino)。 
*** 
## 那么，什么是pymata_aio？
这是[Arduino Firmata](https://github.com/firmata/arduino)的第二代**PyMata**易于使用的应用程序编程接口。它以[Python asyncio库](https://docs.python.org/3/library/asyncio.html)为核心，以实现最高的并发性能。
***
## 包括三个独立的API。
**选择最适合您的工作的一种：**  
**pymata3**  
pymata3 API是在原始PyMata API的基础上建模的，并且对于当前的PyMata用户而言似乎最为熟悉。此API充当pymata_core API的代理，提供了asyncio的所有优点，但无需直接在asyncio中进行编程。  
[单击此处查看说明正在使用的pymata3的示例代码。](https://gist.github.com/MrYsLab/8b735813e413bf62b455)  
**pymata_core**  
此API是纯asyncio方法调用API，适用于希望直接使用asyncio的用户。 它向开发人员公开了其潜在的异步任务/协程/未来模型。  
[单击此处查看说明正在使用的pymata_core的示例代码。](https://gist.github.com/MrYsLab/df8ec22ea16de6c84d67)  
**pymata_iot**  
您想通过*互联网*连接和控制*Arduino*吗？PyMata_IOT是易于运行的WebSocket服务器应用程序，包含在此软件包中。它的API是在应用程序和服务器之间交换的一组JSON消息。因为它使用JSON消息，所以它完全独立于语言。您可以使用Python，JavaScript或您选择的任何其他语言编写WebSocket客户端。  
[单击此处以查看与pymata_iot通信的简单HTML/JavaScript网页示例。](https://gist.github.com/MrYsLab/fc6d9def21832f4b743b)  
它提供与上面其他两个示例完全相同的功能，但是它提供了一个带有两个按钮的网页，用于打开和关闭LED。