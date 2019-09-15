import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)

        file_menu.add_command(label="New file")
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_command(label="About")
        menu.add_command(label="Quit", command=self.destroy)
        self.config(menu=menu)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# Menu()
