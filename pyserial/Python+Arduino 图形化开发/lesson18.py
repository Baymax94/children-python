import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Tkinter app")
        self.iconbitmap("movie.ico")
        self.geometry('400*200+10+10')
        # self.state("zoomed")    # 全屏显示


if __name__ == "__main__":
    app = App()
    app.mainloop()
