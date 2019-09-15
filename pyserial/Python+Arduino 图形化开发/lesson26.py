import serial
import tkinter as tk
ser = serial.Serial('COM7', 9600, timeout=1)

BUTTON_SIZE = 10
NUM_BUTTON = 8
NUM_LIGHTS = NUM_BUTTON * NUM_BUTTON
MARGIN = 2
WINDOW_H = MARGIN + ((BUTTON_SIZE + MARGIN) * NUM_BUTTON)
WINDOW_W = WINDOW_H


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("点亮8X8 LED矩阵")
        self.geometry("300x150")
        self.canvas = tk.Canvas(
            self, width=WINDOW_W, height=WINDOW_H, bg="white")
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.pack()

        self.update()
        self.light = []
        self.status = 0
        for iy in range(NUM_BUTTON):
            for ix in range(NUM_BUTTON):
                x = MARGIN + MARGIN + ((MARGIN + BUTTON_SIZE) * ix)
                y = MARGIN + MARGIN + ((MARGIN + BUTTON_SIZE) * iy)
                self.light.append([
                    0,
                    self.canvas.create_rectangle(
                        x, y, x + BUTTON_SIZE, y + BUTTON_SIZE, fill="blue")
                ])
        print(self.light)

    def mouse_click(self, event):
        items_clicked = self.canvas.find_overlapping(event.x, event.y,
                                                     event.x + 1, event.y + 1)
        # print(items_clicked)
        for item in items_clicked:
            self.light[item - 1][0] = 1 - self.light[item - 1][0]
            if not self.light[item - 1][0]:
                self.canvas.itemconfig(item, fill="blue")
            else:
                self.canvas.itemconfig(item, fill="yellow")

        # print(self.light)
        s = ""
        for i in self.light:
            x, y = i
            s = s + str(x) + "," + str(y) + ","
        s = s[:-1]
        print(s)
        ser.write(s.encode('utf-8'))


if __name__ == "__main__":
    app = App()
    app.mainloop()

# LED点阵
