import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)
COLORS = [("Red", "1"), ("Green", "2"), ("Blue", "3")]


class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("1")
        self.buttons = [self.create_radio(c) for c in COLORS]
        for button in self.buttons:
            # button.pack(anchor=tk.W, padx=10, pady=5)
            button.pack(anchor=tk.W, padx=10, pady=5, side=tk.LEFT)

    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(
            self,
            text=text,
            value=value,
            command=self.set_colorLed,
            variable=self.var)

    def set_colorLed(self):
        color = self.var.get()
        print(color)
        ser.write(color.encode('utf-8'))


'''
    def print_option(self):
        print(self.var.get())
'''

if __name__ == "__main__":
    app = ChoiceApp()
    app.title("单选按钮")
    app.mainloop
