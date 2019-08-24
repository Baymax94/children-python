# 第一个tkinter应用
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="点我", command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Hello, Tkinter!")


if __name__ == "__main__":
    app = App()
    app.title("我的Tkinter应用")
    app.mainloop()