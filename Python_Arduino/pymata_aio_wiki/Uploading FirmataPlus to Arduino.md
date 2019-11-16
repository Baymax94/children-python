# Uploading FirmataPlus to Arduino（将FirmataPlus上传到Arduino）
*FirmataPlus* 是StandardFirmata的增强版本，已包含在此发行版中。  
请注意：*FirmataPlus* 与StandardFirmataPlus不同。StandardFirmataPlus将无法正常工作。  
FirmataPlus提供以下支持：
1. HC-SR04声纳测距仪
2. 旋转编码器（FirmataPlus32u4不支持）
3. 步进电机支持
4. 压电音调产生。

*Leonardo* 和 *Mega 2560* 用户，请上传 *FirmataPlus32u4* 而不是FirmataPlus  
**FirmataPlus** 作为zip文件分发。如果您从Github下载pyamta_aio发行版并解压缩了文件，则将在FirmataPlus目录中找到一个library.zip文件。您也可以在这里[直接](https://github.com/MrYsLab/pymata-aio/blob/master/FirmataPlus/libraries.zip)下载。点击“查看原始文件”按钮进行下载。  
打开Arduino IDE并选择File / Preferences确定您的 *sketchbook* 位置。  

![arduinoSketchDir](https://raw.githubusercontent.com/MrYsLab/pymata-aio/master/documentation/images/arduinoSketchDir.png)  

关闭Arduino IDE，然后将library.zip文件解压缩到 *sketchbook* 位置目录中。  
重新打开Arduino IDE，选择File/Examples/FirmataPlus/FiramataPlus，然后上传到Arduino。  

![firmataplus](https://raw.githubusercontent.com/MrYsLab/pymata-aio/master/documentation/images/firmataplus.png)  

如果在Arduino IDE中编译FirmataPlus草图时看到警告，请确保在“文件/首选项”屏幕中将编译器警告级别设置为“默认”。如果仍然看到警告，请获取libraries.zip的最新副本并重新安装。