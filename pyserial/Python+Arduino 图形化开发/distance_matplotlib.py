import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM9', 9600, timeout=1)

ax = []
ay = []
i = 0

while 1:
    recSer = ser.readline().decode('utf-8').rstrip()
    '''
    if (recSer):
        distance = float(recSer)
        print("距离：", distance)
        time.sleep(0.5)
    '''
    if (recSer):
        distance = float(recSer)
        i = i+0.1
        ax.append(i)
        ay.append(distance)
        plt.clf()
        plt.plot(ax, ay)
        plt.pause(0.1)

# 超声波读取距离数据，通过串口，python对数据进行绘制
