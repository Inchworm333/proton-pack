import time
import random
import gpiozero
import colorzero
import gpiozero.threads

#helpers.py
#has helper functions that might be needed in more than one file.

def mode_decode(modeID):
    inner_mode = modeID % 4
    
    if inner_mode == 0:
        #Proton
        return "proton"
    elif inner_mode == 1:
        #Slime
        return "slime"
    elif inner_mode == 2:
        #Stasis
        return "stasis"
    elif inner_mode == 3:
        #Meson
        return "meson"


def pulse_random_function(self, on_color, off_color, range):
    while True:
        on_time = random.uniform(*range)
        off_time = random.uniform(*range)
        self._blink_device(0, 0, on_time, off_time, on_color, off_color, 1)

gpiozero.RGBLED.pulse_random_function = pulse_random_function

def pulse_random(self, on_color, off_color, range):
    self._blink_thread = gpiozero.threads.GPIOThread(
        self.pulse_random_function,
        (
            on_color, off_color, range
        )
    )
    self._blink_thread.start()

gpiozero.RGBLED.pulse_random = pulse_random

def bubble_function(self, fade_in_time, on_color, off_color):
    while True:
        on_time = random.uniform(*fade_in_time)
        on_color = self.random_RGB(on_color)
        off_color = self.random_RGB(off_color)

        self._blink_device(0, 0, on_time, 0, on_color, off_color, 1, 120)

gpiozero.RGBLED.bubble_function = bubble_function

def bubble_random(self, fade_in_time, on_color, off_color):
    self._blink_thread = gpiozero.threads.GPIOThread(
        self.bubble_function,
        (
            fade_in_time, on_color, off_color
        )
    )
    self._blink_thread.start()

gpiozero.RGBLED.bubble_random = bubble_random

def random_RGB(self, color):
    R = None
    G = None
    B = None
    for i in range(len(color)):
        if i == 0:
            if type(color[0]) is tuple:
                R = random.uniform(*color[0])
            else:
                R = color[0]

        if i == 1:
            if type(color[1]) is tuple:
                G = random.uniform(*color[1])
            else:
                G = color[1]

        if i == 2:
            if type(color[2]) is tuple:
                B = random.uniform(*color[2])
            else:
                B = color[2]
    return (R, G, B)

gpiozero.RGBLED.random_RGB = random_RGB

