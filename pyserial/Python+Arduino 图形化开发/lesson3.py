import serial
import time
ser = serial.Serial('COM7', 9600, timeout=1)
print(ser.name)
data = [1, 2, 3]
while 1:
    valList = [str(x) for x in data]
    sendStr = ','.join(valList)
    print("准备发送的数据： ", sendStr)  # 打印在控制台
    ser.write(sendStr.encode('utf-8'))  # 串口发送数据，编码成比特字符串
    time.sleep(0.1)
    val = ser.readline().decode('utf-8').rstrip()
    if len(val) > 2:
        print("接收到的数据： ", val)
        data = [x + 1 for x in data]
