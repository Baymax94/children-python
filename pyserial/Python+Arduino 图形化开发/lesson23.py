import serial
import time
import threading
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)
isStoped = False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack()
        self.button = tk.Button(self, command=self.printValue, text="打印...")
        self.button.pack(padx=50, pady=10)
        self.update()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        options = {"font": "courier", "fill": "blue", "activefill": "red"}
        self.text_id = self.canvas.create_text((w / 2, h / 2), **options)
        self.text_id2 = self.canvas.create_text((w / 2, h / 2 + 20), **options)
        self.state_action()  # 单独线程

    def state_action(self):
        thread = threading.Thread(target=self.run_action)
        print(threading.main_thread().name)
        print(thread.name)
        thread.start()

    def printValue(self):
        print("你好！")

    def stop_thread(self, event):
        global isStoped
        isStoped = True
        print("停止子线程！")

    def run_action(self):
        while 1:
            val = ser.readline().decode('utf-8')
            parsed = val.split(',')
            # print(parsed)
            parsed = [x.rstrip() for x in parsed]
            if len(parsed) > 1:
                # print(parsed)
                a = int(int(parsed[0] + '0') / 10)
                b = int(int(parsed[1] + '0') / 10)
                print(a)
                print(b)
                self.canvas.itemconfig(self.text_id, text="湿度:{}%".format(a))
                self.canvas.itemconfig(self.text_id2, text="温度:{}*C".format(b))
            time.sleep(2)
            if isStoped:
                break  # 退出线程循环


if __name__ == "__main__":
    app = App()
    app.bind('<Destroy>', app.stop_thread)
    app.mainloop()
