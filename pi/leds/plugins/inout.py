
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    control.red(False)
    control.green(True)
    control.blue(False)
    time.sleep(interval)

    control.red(True)
    control.green(False)
    control.blue(True)
    time.sleep(interval)

