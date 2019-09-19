import serial
import time
ser = serial.Serial('COM7', 9600, timeout=1)
while 1:
    recSer = ser.readline().decode('utf-8').rstrip()
    if (recSer):
        distance = float(recSer)
        print("距离：", distance)
        time.sleep(0.5)
