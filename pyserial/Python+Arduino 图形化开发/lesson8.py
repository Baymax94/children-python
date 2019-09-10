import tkinter as tk


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.login_btn = tk.Button(self, text="登录", command=self.print_login)
        self.clear_btn = tk.Button(self, text="清除", command=self.clear_form)
        self.username.pack()
        self.password.pack()
        self.login_btn.pack(fill=tk.BOTH)  # 当GUITAR窗体大小发生变化时，按钮在X、Y两方向跟随填充
        self.clear_btn.pack(fill=tk.BOTH)

    def print_login(self):
        print("Username:{}".format(self.username.get()))
        print("Password:{}".format(self.password.get()))

    def clear_form(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()  # 获取鼠标焦点


if __name__ == "__main__":
    app = LoginApp()
    app.title("tkinter 登录系统")
    app.mainloop()
