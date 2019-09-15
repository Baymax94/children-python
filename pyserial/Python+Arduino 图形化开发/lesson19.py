import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self, text="Label A", bg="Yellow")
        label_b = tk.Label(self, text="Label B", bg="orange")
        label_c = tk.Label(self, text="Label C", bg="red")
        label_d = tk.Label(self, text="Label D", bg="green")
        label_e = tk.Label(self, text="Label E", bg="blue")

        opts = {'ipadx': 10, 'ipady': 10, 'sticky': 'nswe'}
        label_a.grid(row=0, column=0, **opts)
        # label_a.grid(row=0,column=0,ipadx=10,ipady=10,sticky='nswe')
        label_b.grid(row=1, column=0, **opts)
        label_c.grid(row=0, column=1, rowspan=2, **opts)
        label_d.grid(row=0, column=2, rowspan=2, **opts)
        label_e.grid(row=2, column=0, columnspan=3, **opts)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# grid()布局
