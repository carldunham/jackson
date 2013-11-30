
import random

class Ball:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                self.canvas.move(self.id, 0, 0)
                starts = [2, 3, 4]
                random.shuffle(starts)
                self.x = starts[0]
                random.shuffle(starts)
                self.y = starts[0]
                self.score = 0
                self.score_id = self.canvas.create_text(10, 200, text=self.score)
                self.canvas_height = self.canvas.winfo_height()
                self.canvas_width = self.canvas.winfo_width()

                #print("self.x=%d, self.y=%d" % (self.x, self.y))

        def coords(self):
            return self.canvas.coords(self.id)

        def check(self, paddle):
            paddle_pos = paddle.coords()
            ball_pos = self.coords()

            if self.id in self.canvas.find_overlapping(*paddle_pos):

                x = min(abs(paddle_pos[0] - ball_pos[2]), abs(paddle_pos[2] - ball_pos[0]))
                y = min(abs(paddle_pos[1] - ball_pos[3]), abs(paddle_pos[3] - ball_pos[1]))

                #print("self.x=%d, self.y=%d, x=%d, y=%d" % (self.x, self.y, x, y))

                if x < abs(self.x):
                    self.x = -self.x
                elif y < abs(self.y):
                    self.y = -self.y
                else:
                    print("oops!!")
                    self.x = -self.x
                    self.y = -self.y
                    
                self.score = self.score + 1
                self.canvas.itemconfig(self.score_id, text=self.score)
                #print(self.score)
                                        

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.coords()

            if (pos[1] <= 0) or (pos[3] >= self.canvas_height):
                self.y = -self.y
            if (pos[0] <= 0) or (pos[2] >= self.canvas_width):
                self.x = -self.x















