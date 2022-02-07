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
