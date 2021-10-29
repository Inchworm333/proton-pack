import threading
import gpiozero
import colorzero
import random
import time

class Vent:

    def __init__(self):
        self.led = gpiozero.RGBLED(13,19,26)

        self.colors = []

        self.colors.append(colorzero.Color('#660033'))
        self.colors.append(colorzero.Color('red'))
        self.colors.append(colorzero.Color('r'=1, 'g'=0.27, 'b'=0))
        self.colors.append(colorzero.Color('yellow'))
        self.colors.append(colorzero.Color('white'))

        self.col_num = 0

        self.idle_pulse()

    def idle_pulse(self):
        self.led.pulse(random.random(), random.random(), self.colors[0], self.colors[1])

    def overheat_pulse(self):
        self.col_num = 4
        self.led.pulse(random.uniform(0.3, 0.5), random.uniform(0.3, 0.5), colorzero.Color('white'), colorzero.Color('r'=0.85, 'g'=0.85, 'b'=0.85))

    def fade_off(self):
        while col_num > 0:
            self.led.pulse(0, 3, self.colors[col_num], self.colors[col_num -=1], 1, False)
        self.led.pulse(0, 3, self.colors[0], (0,0,0), 1, False)
        self.led.off()

    def heat_up(self, heating):
        while heating:
            if col_num != 4:
                self.led.pulse(0, 5, self.colors[col_num], self.colors[col_num +=1], 1, False)
            else:
                self.led.color = self.colors[4]

    def cool_down(self, heating):
        while !heating:
            if col_num > 0:
                self.led.pulse(0, 2, self.colors[col_num], self.colors[col_num -=1], 1, False)
            else:
                self.idle_pulse()

    def vent(self):
        self.led.pulse(0, 0.85, (1,1,1), (0,0,0), 1, False)
