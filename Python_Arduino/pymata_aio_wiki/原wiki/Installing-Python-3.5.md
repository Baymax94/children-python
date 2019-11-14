# You must use Python 3.5.X to run pymata_aio 


### **Windows and Mac Users**

To install Python 3.5 or later, go to the [Python home page](https://www.python.org/), and download the latest version of Python 3 for your operating system.

If you have Python 2.7 installed, you do not need to remove it. 

During the installation process, if there is a checkbox to add Python 3.X to your path, make sure it is checked before proceeding with the installation.

![](https://github.com/MrYsLab/s2aio/blob/master/images/pythonInstall.png)

**Linux Users:**

Verify to see if you currently have Python 3.5 or greater installed by opening a terminal window and typing:
```
python3 -V
```
This will return the version of Python 3 installed on your system.

For Linux, if you need to install Python 3, here are the build and installation instructions

1. sudo apt-get update
1. sudo apt-get upgrade
1. sudo apt-get dist-upgrade
1. sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
1. sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
1. sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
1. sudo apt-get install libssl-dev openssl
1. cd ~
1. mkdir build
1. cd build
1. wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz (adjust for latest version of Python 3)
1. tar -zxvf Python-3.6.5.tgz
1. cd Python-3.6.5
1. ./configure
1. make
1. sudo make install

### **After Installation Verify The Python Version**

**Windows Users:**
After installation, open a command window and type: **python -V**. You should see **Python 3.5.2** or something similar.

**Linux Users:**
After installation, open a command window and type: **python3 -V**. You should see **Python 3.5.2** or something similar.