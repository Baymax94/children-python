![logo](https://raw.github.com/MrYsLab/pymata-aio/master/documentation/images/logo.png)

# IMPORTANT NOTE: If you are upgrading to Version 2.22 and use FirmataPlus, please [upgrade your version of FirmataPlus](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-FirmataPlus-to-Arduino) as well. 

# So, what is _pymata_aio_?
It's the _second generation_ of the **PyMata** _easy-to-use,_ application programming interface for [Arduino Firmata](https://github.com/firmata/arduino). It uses the [Python asyncio library](https://docs.python.org/3/library/asyncio.html) at its core, for maximum concurrency performance. 

## Three Independent APIs Are Included.

### Choose the one that is best suited to your job:

### pymata3
The pymata3 API is modeled after the original PyMata API and will seem most familiar to current PyMata users. This API acts as a proxy for the pymata_core API, providing all of the advantages of asyncio,  but without having to directly program in asyncio.

[Click here to see sample code illustrating pymata3 in use.](https://gist.github.com/MrYsLab/8b735813e413bf62b455)

### pymata_core
This API is a  pure asyncio  method call API intended for those who wish to use asyncio directly. It exposes its underlying asyncio _task/coroutine/futures_ model to the developer.

[Click here to see sample code illustrating pymata_core in use.](https://gist.github.com/MrYsLab/df8ec22ea16de6c84d67).
### pymata_iot
Would you like to **_connect_** and control your **_Arduino over the Internet_**? PyMata_IOT is a ready to run, WebSocket server application, included with this package. Its API is a set of JSON messages exchanged between your application and the server. Because it uses JSON messages, it is totally language independent. You can write your WebSocket client using Python, JavaScript or any other language of your choosing. 

[Click here to see a simple HTML/JavaScript web page example that communicates with pymata_iot](https://gist.github.com/MrYsLab/fc6d9def21832f4b743b). 

It provides the exact the same functionality as the other two examples above, but it provides a web page with two buttons to turn the LED on and off.