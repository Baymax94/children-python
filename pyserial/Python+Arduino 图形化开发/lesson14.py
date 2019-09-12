import tkinter as tk
COLORS = [("Red", "red"), ("Green", "green"), ("Blue", "blue")]


class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("red")
        self.buttons = [self.create_radio(c) for c in COLORS]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)
            # button.pack(anchor=tk.W, padx=10, pady=5, side=tk.LEFT)

    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(
            self,
            text=text,
            value=value,
            command=self.print_option,
            variable=self.var)

    def print_option(self):
        print(self.var.get())


if __name__ == "__main__":
    app = ChoiceApp()
    app.title("单选按钮")
    app.mainloop
