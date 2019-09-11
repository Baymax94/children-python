import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.show_message)
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

    def show_message(self, *args):
        value = self.var.get()
        # get()方法返回变量的当前值
        if value:
            text = "hello, {}!".format(value)
        else:
            text = ""
        self.label.config(text=text)  # 标签显示文字


if __name__ == "__main__":
    app = App()
    app.title("标签显示文本")
    app.mainloop
