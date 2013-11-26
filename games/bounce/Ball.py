from tkinter import *
import random
import time

class Ball:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                self.canvas.move(self.id, 245, 100)
                starts = [-3, -2, -1, 1, 2, 3]
                random.shuffle(starts)
                self.x = starts[0]
                self.y = starts[1]
                self.canvas_height = self.canvas.winfo_height()
                self.canvas_width = self.canvas.winfo_width()

        def coords(self):
            return self.canvas.coords(self.id)

        def check(self, paddle):
            paddle_pos = paddle.coords()
            ball_pos = self.coords()
            
            if (ball_pos[2] >= paddle_pos[0]) and (ball_pos[0] <= paddle_pos[2]):
                    
                if ((ball_pos[3] >= paddle_pos[1]) and (ball_pos[3] <= paddle_pos[3])) or ((ball_pos[1] >= paddle_pos[1]) and (ball_pos[1] <= paddle_pos[3])):
                        self.y = -self.y
                        
                
            

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.coords()

            if (pos[1] <= 0) or (pos[3] >= self.canvas_height):
                self.y = -self.y
            if (pos[0] <= 0) or (pos[2] >= self.canvas_width):
                self.x = -self.x















