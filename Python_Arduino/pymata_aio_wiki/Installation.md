# Installation（安装）
# 用pip安装
*pip*安装实用程序包含在Python 3.5中。  
安装：  
打开命令窗口并键入：
```
pip install pymata-aio
```
或
```
sudo pip install pymata-aio
```
这将安装pymata_aio API文件及其所需的外部库。  
*请注意，对于Mac用户，如果您的系统上有多个版本的python（例如2.7.5和3.4.3），则可以尝试使用`[sudo] pip3.5 install pymata-aio`命令来确保已安装pymata-aio，使用正确的Python版本。*
# 从Github安装下载
如果您使用 <https://github.com/MrYsLab/pymata-aio> 上的“下载zip”按钮下载zip文件：  
1. 同时安装pySerial库和websockets库。
2. 使用您喜欢的提取工具，将pymata_aio文件从下载的zip文件中提取到一个方便的目录中。
3. 打开命令窗口并转到目录并验证文件setup.py是否存在。使用Python3类型：
   ```
   python setup.py install
   ```
   或
   ```
   sudo python3 setup.py install
   ```