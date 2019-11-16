# Installing Python 3.5
# 您必须使用Python 3.5.X来运行pymata_aio
## Windows和Mac用户
要安装Python3.5或更高版本，请转到Python主页，然后为您的操作系统下载最新版本的Python 3。  
如果已安装Python 2.7，则无需删除它。  
在安装过程中，如果有一个复选框可将Python 3.X添加到您的路径，请确保在进行安装之前选中它。  
![Python](https://raw.githubusercontent.com/MrYsLab/s2aio/master/images/pythonInstall.png)  
## Linux用户
打开终端窗口并键入以下命令，以查看当前是否安装了Python 3.5或更高版本：
```
python3 -V
```
这将返回系统上安装的Python 3的版本。  
对于Linux，如果您需要安装Python 3，则此处是构建和安装说明
```
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade
    sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
    sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
    sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
    sudo apt-get install libssl-dev openssl
    cd ~
    mkdir build
    cd build
    wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz (adjust for latest version of Python 3)
    tar -zxvf Python-3.6.5.tgz
    cd Python-3.6.5
    ./configure
    make
    sudo make install
```
## 安装后验证Python版本
Windows用户：安装后，打开命令窗口并键入：python -V。 您应该看到Python 3.5.2或类似的东西。  
Linux用户：安装后，打开命令窗口并输入：python3 -V。 您应该看到Python 3.5.2或类似的东西。