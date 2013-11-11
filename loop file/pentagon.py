import turtle
import math
from random import *

sides = 5.564564357453685468973543765874547563876
di = 200
count = sides

size = (3.1415926 * di) / sides
turn = 360 / count
angle = 360 / sides

print("sides=%d, count=%d, size=%d" % (sides, count, size))

# ONLY MULTIPLUS OF 360 IN TURN VARIABLE

t = turtle.Pen()

while True:
    r = random()
    g = random()
    b = random()

    t.color(r,g,b)

    #t.begin_fill()

    for j in range(round(sides)):
        t.left(angle)
        t.forward(size)

    #t.end_fill()

    t.left(turn)
