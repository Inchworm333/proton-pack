import threading
import gpiozero
import colorzero

class Vent:

    def __init__(self):
        self.led = gpiozero.RGBLED(13,19,26)

        self.colors = []

        #self.colors.append(colorzero.Color(
