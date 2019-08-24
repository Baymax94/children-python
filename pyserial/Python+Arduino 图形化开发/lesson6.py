# tkinter按钮
import tkinter as tk
RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]

# 定义按钮的relief属性，即按钮的样式


class ButtonsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.img = tk.PhotoImage(
            file=
            "E:\GitHub\children-python\pyserial\Python+Arduino 图形化开发\Baymax0823.png"
        )
        self.btn = tk.Button(
            self,
            text="图片按钮",
            image=self.img,
            compound=tk.LEFT,  # compound参数设置图片相对于文字的位置
            command=self.disable_btn)
        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()
        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=tk.LEFT)

    def create_btn(self, relief):
        # print("Hello, Tkinter!")
        return tk.Button(self, text=relief, relief=relief)

    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = ButtonsApp()
    app.title("我的Tkinter应用")
    app.mainloop()
