import turtle
from random import *

sides = randint(3,20)
count = randint(10,100)
size = randint(1,100)

turn = 360 / count
angle = 360 / sides

print("sides=%d, count=%d, size=%d" % (sides, count, size))

# ONLY MULTIPLUS OF 360 IN TURN VARIABLE

t = turtle.Pen()

for i in range(count):
    r = random()
    g = random()
    b = random()

    t.color(r,g,b)

    t.begin_fill()

    for j in range(sides):
        t.left(angle)
        t.forward(size)

    t.end_fill()

    t.left(turn)
