from tkinter import *
import random
import time

class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        canvas.bind_all('<KeyPress-Left>', self.move_left)
        canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas_width = self.canvas.winfo_width()

    def coords(self):
        return self.canvas.coords(self.id)
    
    def move_left(self, event):
        #print (event.keysym)
        pos = self.coords()
        if pos[0] > 0:
            self.canvas.move(self.id, -10, 0)
 
    def move_right(self, event):
        #print (event.keysym)
        pos = self.coords()
        if pos[2] < self.canvas_width:
            self.canvas.move(self.id, 10, 0)    

    def draw(self):
        pass
