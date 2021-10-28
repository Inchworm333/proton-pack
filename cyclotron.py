import threading
import time
import gpiozero
import colorzero
import helpers
import random

class Cyclotron:

    def __init__(self):
        self.leds = []
        self.leds.append(gpiozero.RGBLED(0,1,2))
        self.leds.append(gpiozero.RGBLED(3,4,5))
        self.leds.append(gpiozero.RGBLED(6,7,8))
        self.leds.append(gpiozero.RGBLED(9,10,11))
        
        self.thread = None
        self.color = "purple"
        self.speed = 0.75
        self.start_spin()

    def spin_function(self, color, speed):
        while self.spin:
            for led in self.leds:
                led.color = colorzero.Color(color)
                #led.pulse(1, 1, (1,0,0), (1,0.5,0.5))
                time.sleep(speed)
                led.off()

    def start_spin(self):
        self.spin = True
        self.thread = threading.Thread(target=self.spin_function, args=(self.color, self.speed))
        self.thread.start()

    def stop_spin(self):
        self.spin = False

    def mode():
        global mode
        
        mode_decoded = mode_decode(mode)

        if mode_decoded == "proton":
            self.color = "red"
        elif mode_decoded == "slime":
            self.color = "green"
        elif mode_decoded == "stasis":
            self.color = "blue"
        elif mode_decoded == "meson":
            self.color = "yellow"
cyclotron = Cyclotron()

