import gpiozero
import threading

class FiringStatusLeds:

    def __init__(self):
        self.leds = {}
        self.thread = None

        self.leds['green'] = gpiozero.PWMLED(17)
        self.leds['yellow'] = gpiozero.PWMLED(16)
        self.leds['red'] = gpiozero.PWMLED(15)

        self.speed = 0.25

    def blink(self, color): 
        self.leds[color].blink(self.speed, self.speed)

    def all_on(self):
        for key, value in self.leds.items():
            value.on()

    def all_off(self):
        for key, value in self.leds.items():
            value.off()
    
    def fade_off(self):
        for key, value in self.leds.items():
            value.pulse(0, 3, 1)
        self.all_off()

    def kill_all(self):
        for name, led in self.leds.items():
            led.close()
