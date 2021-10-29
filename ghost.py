import threading
import time
from enum import Enum
import gpiozero
import colorzero
import pigpio
import sys
import signal

#Importing other files
from cyclotron import Cyclotron
from status import FiringStatusLeds
from wand import proton_reader
import helpers

#SHOOTING MODE VARIABLE
mode = 0

def main():
 
    PWM_GPIO = 12     
    PWM_RUN_TIME = 60.0
    PWM_SAMPLE_TIME = 2.0

    #cyclotron
    cyclotron = None
    statusleds = None


    while True:

        pi = pigpio.pi()

        wand_PWM = proton_reader(pi, PWM_GPIO)

        start = time.time()

        global mode

        while (time.time() - start) < PWM_RUN_TIME:
            
            time.sleep(PWM_SAMPLE_TIME)

            wand_pulse_val = wand_PWM.pulse_width()

            if(wand_pulse_val is not None):
                wand_pulse = wand_pulse_val // 1000

                print(wand_pulse)

                if near(wand_pulse, 8):
                    #Power Up
                    print('power up')
                    #SOUNDS HERE
                    cyclotron = Cyclotron()
                    statusleds = FiringStatusLeds()
                    break
                elif near(wand_pulse, 14):
                    #Power Down
                    print('power down')
                    #SOUNDS HERE
                    cyclotron.fade_off()
                    statusleds.fade_off()
                    mode = 0
                    break
                elif near(wand_pulse, 20):
                    #Overheat start
                    print('overheat started')
                    #SOUNDS HERE
                    break
                elif near(wand_pulse, 26):
                    #Vent Start (manual or auto)
                    print('venting started')
                    #SOUNDS HERE
                    break
                elif near(wand_pulse, 32):
                    #Mode Change
                    print('Mode Changed')
                    mode += 1
                    print("Mode = " + helpers.mode_decode(mode))
                    #TODO will need to edit cyclotron.py to add sound files
                    cyclotron.mode()
                    break
                elif near(wand_pulse, 38):
                    #Song Request
                    print('playing song')
                    #SONGS HERE
                    break
                elif near(wand_pulse, 44):
                    #Intense Fire ON
                    print('intense fire on')
                    #SOUNDS HERE
                    break
                elif near(wand_pulse, 50):
                    #Intense Fire OFF
                    print('Intense fire off')
                    #SOUNDS HERE
                    break
                elif near(wand_pulse, 56):
                    #Power Down with sound
                    print('power down (with sound)')
                    #SOUNDS HERE
                    cyclotron.fade_off()
                    statusleds.fade_off()
                    mode = 0
                    break
                wand_pulse_val = None
            else:
                print('wand_pulse_val is None')

def near(number, ideal):
    return abs(number - ideal) <= 3

main()


