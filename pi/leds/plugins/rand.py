
import random
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    n = random.randint(0, 7)

    control.alloff()
    time.sleep(0.02)  # so we can see repeats

    control.red(n & 0b100)
    control.green(n & 0b010)
    control.blue(n & 0b001)

    time.sleep(interval)
