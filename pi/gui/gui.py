#!/usr/bin/env python
import math
import Tkinter as tk
import urllib2
import json


class Window(tk.Frame):
    def __init__(self, master=None):
        self.objects = []
        self.width = self.mm_to_pix(3000)
        self.height = self.mm_to_pix(2000)
        tk.Frame.__init__(self, master)
        self.grid()

        # last create objects
        self.createWidgets()

    def clean(self):
        for o in self.objects:
            self.canvas.delete(o)

    def transform_to_window_coord(self, x=0, y=0):
        x, y = self.mm_to_pix(x + 1500), self.mm_to_pix(y)
        assert(0 <= x <= self.width)
        assert(0 <= y <= self.width)
        return x, y

    def mm_to_pix(self, mm):
        return int(mm * 0.3)

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()

    def query_server(self):
        """ obtain the list of object to display """

        response = urllib2.urlopen('http://127.0.0.1:5000/table')
        table_objects = json.load(response)
        return table_objects

    def display_obj(self):
        try:
            obj = self.query_server()
            self.clean()
            self.objects.append(self.big_robot(obj['big_robot']))
            self.objects.append(self.small_robot(obj['small_robot']))
            for r in obj['other_robots']:
                self.objects.append(self.small_robot(r, 'red'))
        except:
            print "did not reach server"

        self.after(50, self.display_obj)

    def big_robot(self, br, color='blue'):
        return self.default_robot(br['x'], br['y'], br['cap'], color=color)

    def small_robot(self, br, color='blue'):
        return self.default_robot(
            br['x'], br['y'],
            br['cap'], sizex=20, sizey=15, color='red')

    def default_robot(self, x, y, cap, sizex=80, sizey=50, color='blue'):
        x, y = self.transform_to_window_coord(x, y)
        assert(sizex > 0)
        assert(sizey > 0)
        points = [
            x + (math.cos(cap) * sizex - math.sin(cap) * sizey),
            y + (math.sin(cap) * sizex + math.cos(cap) * sizey),
            x + (math.cos(cap) * sizex + math.sin(cap) * sizey),
            y + (math.sin(cap) * sizex - math.cos(cap) * sizey),
            x - (math.cos(cap) * sizex - math.sin(cap) * sizey),
            y - (math.sin(cap) * sizex + math.cos(cap) * sizey),
            x - (math.cos(cap) * sizex + math.sin(cap) * sizey),
            y - (math.sin(cap) * sizex - math.cos(cap) * sizey),
            ]
        return self.canvas.create_polygon(points, fill=color)

if __name__ == "__main__":
    app = Window()
    app.master.title('Sample application')
    app.after(50, app.display_obj)
    app.mainloop()
