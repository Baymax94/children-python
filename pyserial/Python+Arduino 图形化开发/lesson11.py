import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.set_brightness)
        # "w":当变量写入时调用
        # "r":当变量被读取时调用
        # "u" (for unset):当变量被删除时调用
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(
            self, text="Clear",
            command=lambda: self.var.set(""))  # set()方法更新变量的值
        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()

    def set_brightness(self, *args):
        value = self.var.get()
        # get()方法返回变量的当前值
        try:
            value = int(value)
        except ValueError:
            ser.write('0'.encode('utf-8'))
            text = "请输入0-255之间的一个整数！"
            self.label.config(text=text)  # 标签显示文字
        if isinstance(value, int):
            if 0 <= value <= 255:
                ser.write(str(value).encode('utf-8'))
                text = "LED亮度为：{}!".format(value)
            else:
                ser.write('0'.encode('utf-8'))
                text = "LED亮度范围是0~255"
            self.label.config(text=text)  # 标签显示文字


'''
    def set_brightness(self, *args):
        value = self.var.get()
        # get()方法返回变量的当前值
        if value:
            text = "hello, {}!".format(value)
        else:
            text = ""
        self.label.config(text=text)  # 标签显示文字
'''

if __name__ == "__main__":
    app = App()
    app.title("标签显示文本")
    app.mainloop
