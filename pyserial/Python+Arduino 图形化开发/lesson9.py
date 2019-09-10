import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)


class BrightnessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.brightness = tk.Entry(self)
        self.set_btn = tk.Button(
            self, text="设置亮度", command=self.set_brightness)
        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_form)
        self.brightness.pack()
        self.set_btn.pack(fill=tk.BOTH)  # 当GUITAR窗体大小发生变化时，按钮在X、Y两方向跟随填充
        self.clear_btn.pack(fill=tk.BOTH)

    def set_brightness(self):
        ser.write(self.brightness.get().encode('utf-8'))  # 串口发送数据，编码成比特字符串

    def clear_form(self):
        self.brightness.delete(0, tk.END)
        ser.write('0'.encode('utf-8'))  # 串口发送数据，编码成比特字符串
        self.brightness.focus_set()  # 获取鼠标焦点


if __name__ == "__main__":
    app = BrightnessApp()
    app.title("文本输入框控制arduino LED灯亮度")
    app.mainloop
