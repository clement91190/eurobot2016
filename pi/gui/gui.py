#!/usr/bin/env python
import Tkinter as tk
import random


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.width = self.mm_to_pix(3000)
        self.height = self.mm_to_pix(2000)
        self.createWidgets()
        self.rectangle = None

    def mm_to_pix(self, mm):
        return int(mm * 0.3)

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()

    def query_server(self):
        """ obtain the list of object to display """
        pass

    def random_rectangle(self):
        x, y, x1, y1 = random.randint(0, 100), random.randint(0, 100), random.randint(0, self.width), random.randint(0, self.height)
        if self.rectangle:
            self.canvas.delete(self.rectangle)
        self.rectangle = self.canvas.create_rectangle(x, y, x1, y1, fill='blue')
        self.after(500, self.random_rectangle)

app = Window()
app.master.title('Sample application')
app.after(500, app.random_rectangle)
app.mainloop()



