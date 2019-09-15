import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.checked = tk.BooleanVar()
        self.checked.trace("w", self.mark_checked)
        self.radio = tk.StringVar()
        self.radio.set("1")
        self.radio.trace("w", self.mark_radio)

        menu = tk.Menu(self)
        submenu = tk.Menu(menu, tearoff=0)

        submenu.add_checkbutton(
            label="Checkbutton",
            onvalue=True,
            offvalue=False,
            variable=self.checked)
        submenu.add_separator()
        submenu.add_radiobutton(label="red", value="1", variable=self.radio)
        submenu.add_radiobutton(label="green", value="2", variable=self.radio)
        submenu.add_radiobutton(label="blue", value="3", variable=self.radio)

        menu.add_cascade(label="colorLED", menu=submenu)
        menu.add_command(label="Quit", command=self.destroy)
        self.config(menu=menu)

    def mark_checked(self, *args):
        print(self.checked.get())

    def mark_radio(self, *args):
        value = self.radio.get()
        print(value)
        ser.write(value.encode('utf-8'))


if __name__ == "__main__":
    app = App()
    app.mainloop()
