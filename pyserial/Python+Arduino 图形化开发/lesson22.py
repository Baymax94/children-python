import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("画布文字")
        self.geometry("300x100")

        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.canvas = tk.Canvas(self, bg="white")

        self.entry.pack(pady=5)
        self.canvas.pack()
        self.update()

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        options = {"font": "courier", "fill": "blue", "activefill": "red"}
        self.text_id = self.canvas.create_text((w / 2, h / 2), **options)
        self.var.trace("w", self.write_text)

    def write_text(self, *args):
        self.canvas.itemconfig(self.text_id, text=self.var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
