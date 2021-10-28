from enum import Enum
import gpiozero
import threading

class FiringStatusLeds:

    def __init__(self):
        self.leds = {}
        self.thread = None

        self.leds['green'] = LED(17)
        self.leds['yellow'] = LED(16)
        self.leds['red'] = LED(15)

        self.all_on()

    def blink(self, color, speed): 
        self.all_on()
        self.leds[color].blink(speed, speed)

    def all_on(self):
        for value in self.leds.items():
            value.on()

    def all_off(self):
        for value in self.leds.items():
            value.off()
