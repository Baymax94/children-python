import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.scale = tk.Scale(
            self,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            command=self.set_brightness)
        self.btn = tk.Button(self, text="复位", command=self.reset)
        self.scale.pack()
        self.btn.pack()

    def set_brightness(self, value):
        print(value)
        for i in range(10):
            ser.write(str(value).encode('utf-8'))

    def reset(self):
        self.scale.set(0)
        print("Scale: {}".format(self.scale.get()))


if __name__ == "__main__":
    app = App()
    app.title("滑杆控制LED灯亮度")
    app.mainloop
