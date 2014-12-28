
import random
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    n = random.randint(0, 7)

    control.red(n & 0b100)
    control.green(n & 0b010)
    control.blue(n & 0b001)

    time.sleep(interval)
