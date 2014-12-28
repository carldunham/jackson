
import time

import control


def setup():
    pass


def teardown():
    pass


def step(interval):
    control.blue(False)  # maybe from the last step
    control.red(True)
    time.sleep(interval)

    control.red(False)
    control.green(True)
    time.sleep(interval)

    control.green(False)
    control.blue(True)
    time.sleep(interval)
