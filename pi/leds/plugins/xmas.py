
# like rand, but without those un-festive pauses and darkness
# plus, let's twinkle a bit!
#
import random
import time

import control

_last = -1


def setup():
    pass


def teardown():
    pass


def step(interval):
    n = random.randint(1, 7)

    global _last

    while n == _last:
        n = random.randint(1, 7)

    _last = n

    control.red(n & 0b100)
    control.green(n & 0b010)
    control.blue(n & 0b001)

    time.sleep(interval * random.gauss(0.0, 0.5))
