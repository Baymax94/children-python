import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)


class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var_R = tk.IntVar()
        self.var_G = tk.IntVar()
        self.var_B = tk.IntVar()
        self.vars = [self.var_R, self.var_G, self.var_B]
        self.cb_R = tk.Checkbutton(
            text="red？", variable=self.var_R, command=self.set_color)
        self.cb_G = tk.Checkbutton(
            text="green？", variable=self.var_G, command=self.set_color)
        self.cb_B = tk.Checkbutton(
            text="blue？", variable=self.var_B, command=self.set_color)
        self.cbs = [self.cb_R, self.cb_G, self.cb_B]
        for cb in self.cbs:
            cb.pack(anchor=tk.W, padx=10, pady=5)

    def set_color(self):
        values = []
        for i in self.vars:
            values.append(i.get())
        print(values)
        values = [str(v) for v in values]
        values = ",".join(values)
        ser.write(values.encode('utf-8'))


if __name__ == "__main__":
    app = SwitchApp()
    app.title("TK复选框")
    app.mainloop()
