from enum import Enum
import gpiozero
import threading

class FiringStatusLeds:

    def __init__(self):
        self.leds = {}
        self.thread = None

        self.leds['green'] = gpiozero.LED(17)
        self.leds['yellow'] = gpiozero.LED(16)
        self.leds['red'] = gpiozero.LED(15)

        self.speed = 0.25

        self.all_on()
        self.blink('green')

    def blink(self, color): 
        self.all_on()
        self.leds[color].blink(self.speed, self.speed)

    def all_on(self):
        for key, value in self.leds.items():
            value.on()

    def all_off(self):
        for key, value in self.leds.items():
            value.off()
