
import RPi.GPIO as GPIO

ON = GPIO.HIGH
OFF = GPIO.LOW

LED_R = 12
LED_G = 16
LED_B = 21

ALL_LEDS = [LED_R, LED_G, LED_B]


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)

    alloff()


def teardown():
    alloff()
    GPIO.cleanup()


def set(which, on=True):
    GPIO.output(which, ON if on else OFF)


def on(which):
    set(which, ON)


def off(which):
    set(which, OFF)


def red(on=True):
    set(LED_R, on)


def green(on=True):
    set(LED_G, on)


def blue(on=True):
    set(LED_B, on)


def all(on=True):
    [set(p, on) for p in ALL_LEDS]


def allon():
    all(ON)


def alloff():
    all(OFF)
