import threading
import time
import gpiozero
import colorzero
import helpers

class Cyclotron:

    def __init__(self):
        self.leds = []
        self.leds.append(gpiozero.RGBLED(0,1,2))
        self.leds.append(gpiozero.RGBLED(3,4,5))
        self.leds.append(gpiozero.RGBLED(6,7,8))
        self.leds.append(gpiozero.RGBLED(9,10,11))
        
        self.color = "red"
        self.speed = 0.5
        self.spin = True
        self.start_spin

    def start_spin():
        self.spin = True
        threading.Thread(None, spin_function, (self.color, self.speed), {}, True)

    def stop_spin():
        self.spin = False

    def spin_function(color, speed):
        while self.spin:
            for led in self.leds:
                led.color = Color(color)
                sleep(speed)

    def mode():
        global mode
        
        mode_decoded = mode_decode(mode)

        if mode_decoded == "proton":
            self.color = "red"
        elif mode_decoded == "slime":
            self.color = "green"
        elif mode_decoded == "stasis":
            self.color = "red"
            #TODO check with philip on color and speeds
        elif mode_decoded == "meson":
            self.color = "red"
