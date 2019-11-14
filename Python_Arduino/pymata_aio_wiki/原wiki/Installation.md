# Installing with _pip_
The **_pip_** installation utility is included with Python 3.5. 

To install:

Open a command window and type:

`pip install pymata-aio`

or

`sudo pip install pymata-aio`


This will install the pymata_aio API files and their required external libraries.

_Note, for Mac users, if you have multiple versions of python on your system (for example 2.7.5 and 3.4.3) you might try the command [sudo] pip3.5 install pymata-aio to make sure pymata-aio is installed for the correct Python version._
# Installing From A _Github Download_
If you download the zip file using the _download zip_ button on https://github.com/MrYsLab/pymata-aio:

1. Install both the [pySerial](https://github.com/pyserial/pyserial) library and [websockets](https://github.com/aaugustin/websockets) library.
1. Using your favorite extraction tool, extract the pymata_aio files from the downloaded zip file to a convenient directory.
1. Open a command window and go to the directory and verify that the file _setup.py_ is present.Using Python3 type:

`python setup.py install`

or

`sudo python3 setup.py install`