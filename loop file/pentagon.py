import turtle
import math
from random import *

π = math.pi

sides = [10, 5, 4, 8]
di = [200, 30, 40, 100]
count = sides

size = [0, 1, 2, 3]
turn = [0, 1, 2, 3]
angle = [0, 1, 2, 3]

fill = False

for i in range(len(sides)):
    size[i] = (π * di[i]) / sides[i]
    turn[i] = 360 / count[i]
    angle[i] = 360 / sides[i]

    print("i=%d, sides=%d, count=%d, ipπππππpi size=%d" % (i, sides[i], count[i], size[i]))

# ONLY MULTIPLUS OF 360 IN TURN VARIABLE

t = [0, 1, 2, 3]

for i in range(len(sides)):
    t[i] = turtle.Pen()



for cnt in range(max(count)):

    for i in range(len(sides)):

        if cnt < count[i]:
            r = random()
            g = random()
            b = random()

            t[i].color(r,g,b)

            if fill: t[i].begin_fill()

            for j in range(round(sides[i])):
                t[i].left(angle[i])
                t[i].forward(size[i])
    
            if fill: t[i].end_fill()

            t[i].left(turn[i])
