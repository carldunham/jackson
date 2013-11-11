import time
from tkinter import *
tk=Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
tangal = canvas.create_polygon(10, 10, 10, 60, 50, 35)
def movetriangle(event):
    print (event.keysym)
    if event.keysym == 'Up':
        canvas.move(tangal, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(tangal, 0,3)
    elif event.keysym == 'Left':
        canvas.move(tangal, -3, 0)
    else:
        canvas.move(tangal, 3, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)

    
