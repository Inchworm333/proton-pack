import threading
import time
from enum import Enum
import gpiozero
import colorzero
import pigpio
import sys
import signal

#Importing other files
import wand

#LED color enums
class LedColor(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

#global variables
firing = False

#Threads
#threading.Thread(group="pack", 

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
    greenLed = FiringStatusLed(LedColor.GREEN, LED(17))
    yellowLed = FiringStatusLed(LedColor.YELLOW, LED(16))
    redLed = FiringStatusLed(LedColor.RED, LED(15))

    #THREADS
    #threading.Thread(None, wand_read_loop, 'Wand Read', (PWM_GPIO, PWM_RUN_TIME, PWM_SAMPLE_TIME))

    #TODO remove this probably
    #signal.pause()
    wand_read_loop(PWM_GPIO, PWM_RUN_TIME, PWM_SAMPLE_TIME)


mode = 0 

def wand_read_loop(GPIO, total_time, sample_time):
    
    while True:

        pi = pigpio.pi()

        wand_PWM = proton_reader(pi, GPIO)

        start = time.time()

        global mode

        while (time.time() - start) < total_time:
            
            time.sleep(sample_time)

            wand_pulse_val = wand_PWM.pulse_width()

            if(wand_pulse_val is not None):
                wand_pulse = wand_pulse_val // 1000

                print(wand_pulse)

                if near(wand_pulse, 8):
                    #Power Up
                    print('power up')
                    break
                elif near(wand_pulse, 14):
                    #Power Down
                    print('power down')
                    mode = 0
                    break
                elif near(wand_pulse, 20):
                    #Overheat start
                    print('overheat started')
                    break
                elif near(wand_pulse, 26):
                    #Vent Start (manual or auto)
                    print('venting started')
                    break
                elif near(wand_pulse, 32):
                    #Mode Change
                    print('Mode Changed')
                    mode += 1
                    mode_decode(mode)
                    break
                elif near(wand_pulse, 38):
                    #Song Request
                    print('playing song')
                    break
                elif near(wand_pulse, 44):
                    #Intense Fire ON
                    print('intense fire on')
                    break
                elif near(wand_pulse, 50):
                    #Intense Fire OFF
                    print('Intense fire off')
                    break
                elif near(wand_pulse, 56):
                    #Power Down with sound
                    print('power down (with sound)')
                    break
                wand_pulse_val = None
            else:
                print('wand_pulse_val is None')

def near(number, ideal):
    return abs(number - ideal) <= 3

def mode_decode(modeID):
    inner_mode = modeID % 4
    print(inner_mode)
    
    if inner_mode == 0:
        #Proton
        print('Shooting Mode: Proton')
        None
    elif inner_mode == 1:
        #Slime
        print('Shooting Mode: Slime')
        None
    elif inner_mode == 2:
        #Stasis
        print('Shooting Mode: Stasis')
        None
    elif inner_mode == 3:
        #Meson
        print('Shooting Mode: Meson')
        None
main()


class cyclotron:

    def __init__(self):
        self.leds = []
        self.leds.append(RGBLED(0,1,2))
        self.leds.append(RGBLED(3,4,5))
        self.leds.append(RGBLED(6,7,8))
        self.leds.append(RGBLED(9,10,11))
