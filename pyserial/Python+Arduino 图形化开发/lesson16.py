import tkinter as tk


class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.cb = tk.Checkbutton(
            self, text="点亮？", variable=self.var, command=self.print_value)
        self.cb.pack(padx=100, pady=10)

    def print_value(self):
        print(self.var.get())


if __name__ == "__main__":
    app = SwitchApp()
    app.title("TK复选框")
    app.mainloop()