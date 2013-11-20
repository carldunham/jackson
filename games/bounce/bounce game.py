from tkinter import *
import random
import time
from Ball import Ball
from Paddle import Paddle

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()



ball = Ball(canvas, 'blue')
paddle = Paddle(canvas, 'green')
while 1:
    paddle.draw()
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.00000001)
 
