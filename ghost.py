import threading
import time
from enum import Enum
import gpiozero
import colorzero
import pigpio
import sys
import signal

sys.path.append(".")

#Importing other files
import wand
from cyclotron import Cyclotron

#LED color enums
class LedColor(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

#global variables
firing = False

class FiringStatusLed:
    
    leds = []

    def __init__(self, color, led):
        self.color = color
        self.led = led
        self.led.on()
        self.is_blinking = False
        self.leds.append(self)

    
    def blink(self):
        self.is_blinking = True
        for led in self.leds:
            if(led != self):
                led.is_blinking = False
                led.led.on()
        while(self.blink):
            self.led.off()
            time.sleep(0.5)
            self.led.on()
            time.sleep(0.5)


def main():
 
    PWM_GPIO = 12 #TODO: find better gpio
    PWM_RUN_TIME = 60.0
    PWM_SAMPLE_TIME = 2.0

    #LED setups
    #greenLed = FiringStatusLed(LedColor.GREEN, LED(17))
    #yellowLed = FiringStatusLed(LedColor.YELLOW, LED(16))
    #redLed = FiringStatusLed(LedColor.RED, LED(15))

    #cyclotron
    cyclotron = Cyclotron()

    #THREADS
    #threading.Thread(None, wand_read_loop, 'Wand Read', (PWM_GPIO, PWM_RUN_TIME, PWM_SAMPLE_TIME))

    #TODO remove this probably
    signal.pause()
    #wand_read_loop(PWM_GPIO, PWM_RUN_TIME, PWM_SAMPLE_TIME)


main()


