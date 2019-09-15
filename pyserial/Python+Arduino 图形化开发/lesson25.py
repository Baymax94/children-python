import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)
LED_ON = '1'
LED_OFF = '0'


class ButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn_on = tk.Button(
            self, text="打开", relief=tk.RAISED, command=self.on)
        self.btn_off = tk.Button(
            self, text="关闭", relief=tk.RAISED, command=self.off)
        self.btn_on.pack(padx=40, pady=10, side=tk.LEFT)
        self.btn_off.pack(padx=40, pady=10, side=tk.LEFT)

    def on(self):
        ser.write(LED_ON.encode('utf-8'))  # 串口发送数据，编码成比特字符串
        print("LED 打开了！")

    def off(self):
        ser.write(LED_OFF.encode('utf-8'))  # 串口发送数据，编码成比特字符串
        print("LED 关闭了！")


if __name__ == "__main__":
    app = ButtonsApp()
    app.title("按钮控制arduino LED灯")
    app.mainloop()

# 蓝牙串口通信
