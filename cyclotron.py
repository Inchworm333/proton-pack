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
        
        self.thread = None
        self.color = "red"
        self.speed = 0.85
        self.start_spin()

    def spin_function(self):
        while self.spin:
            for led in self.leds:
                led.color = colorzero.Color(self.color)
                time.sleep(self.speed)
                led.off()

    def spin_fade_function(self):
        while self.spin:
            for led in self.leds:
                led.pulse(self.speed/2, self.speed/2, colorzero.Color(self.color))
                time.sleep(self.speed)
                led.off()

    def start_spin(self, spin_func):
        self.spin = True
        self.thread = threading.Thread(target=spin_func)
        self.thread.start()

    def stop_spin(self):
        self.spin = False
        for led in self.leds:
            led.off()

    def all_on(self):
        for led in self.leds:
            led.color = self.color

    def mode():
        global mode
        
        mode_decoded = mode_decode(mode)

        if mode_decoded == "proton":
            #SOUNDS HERE
            self.color = "red"
            self.stop_spin()
            self.start_spin(self.spin_function)
        elif mode_decoded == "slime":
            #SOUNDS HERE
            self.color = "green"
            self.stop_spin()
            self.slime_bubble_start()
        elif mode_decoded == "stasis":
            #SOUNDS HERE
            self.color = "blue"
            self.stop_spin()
            self.start_spin(self.spin_fade_function)
        elif mode_decoded == "meson":
            #SOUNDS HERE
            self.color = "yellow"
            self.stop_spin()
            self.start_spin(self.spin_function)

    def fade_off(self):
        global mode

        if mode_decode(mode) != "slime":
            for led in self.leds:
                if led.is_lit():
                    led.pulse(0, 3, led.color, (0,0,0), 1)
                    led.off()
        else:
            self.all_on()
            self.leds[0].pulse(0, 1.5, (0.05, 1, 0.08), (0,0,0), 1)
            self.leds[1].pulse(0, 1.5, (0.05, 1, 0.08), (0,0,0), 1, True)
            self.leds[0].off()
            self.leds[1].off()
            self.leds[2].pulse(0, 1.5, (0.05, 1, 0.08), (0,0,0), 1)
            self.leds[3].pulse(0, 1.5, (0.05, 1, 0.08), (0,0,0), 1, True)
            self.leds[2].off()
            self.leds[3].off()

    def slime_bubble_function(self, led):
        led.pulse(random.uniform(0.3, 1.8), 0, (0.05, random.uniform(0.73, 0.97), 0.08), (0.05, random.uniform(0.48, 0.67), 0.08))

    def slime_bubble_start(self):
        for led in self.leds:
            slime_bubble_function(led)
