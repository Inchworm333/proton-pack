#!/usr/bin/python3
import time
import gpiozero
import colorzero
import pigpio
import sys
import signal
from sound_player import Sound, Playlist, SoundPlayer
import daemon

#Importing other files
from cyclotron import Cyclotron
from status import FiringStatusLeds
from wand import proton_reader
from vent import Vent
from background import Background
import helpers

sound = Sound("/root/sounds/spark6.wav")
sound.play()

#SHOOTING MODE VARIABLE
mode = 0
heating = False
wand_pulse_val = None

# Error file output
errorLog = "/root/ghostLogs/ghostError.log"
generalError = open("/root/ghostLogs/generalError.log", "w+")

def main():
 
    PWM_GPIO = 12     
    PWM_RUN_TIME = 60.0
    PWM_SAMPLE_TIME = 2.0

    #cyclotron
    cyclotron = None
    statusleds = None
    vent = None
    background = None
    last = 'power down'

    debug = False
    print(sys.argv)
    if len(sys.argv) > 1:
        debug = True
        print("debugging mode on")


    while True:

        pi = pigpio.pi()

        wand_PWM = proton_reader(pi, PWM_GPIO)

        start = time.time()

        global mode
        global heating
        global wand_pulse_val

        while (time.time() - start) < PWM_RUN_TIME:
            
            time.sleep(PWM_SAMPLE_TIME)

            wand_pulse_val = wand_PWM.pulse_width()

            if(wand_pulse_val is not None):
                wand_pulse = wand_pulse_val // 1000
                
                if debug:
                    print(wand_pulse)

                if near(wand_pulse, 8):
                    #Power Up
                    if debug:
                        print('power up')
                    sound = Sound("/root/sounds/protongun_powerup.wav")
                    sound.play()
                    cyclotron = Cyclotron()
                    statusleds = FiringStatusLeds()
                    vent = Vent()
                    time.sleep(3)
                    bgsound = Background()
                    last = 'power up'
                    break
                elif near(wand_pulse, 14):
                    #Power Down
                    if debug:
                        print('power down')
                    #SOUNDS HERE
                    if last != 'power down':
                        sound = Sound("/root/sounds/power_down_2.wav")
                        sound.play()
                        time.sleep(0.5)
                        bgsound.stopbg()
                    if cyclotron is not None:
                        cyclotron.fade_off(mode)
                    if statusleds is not None:
                        statusleds.fade_off()
                    if vent is not None:
                        vent.fade_off()
                    cyclotron = None
                    statusleds = None
                    vent = None
                    mode = 0
                    last = 'power down'
                    break
                elif near(wand_pulse, 20):
                    #Overheat start
                    if debug:
                        print('overheat started')
                    #SOUNDS HERE
                    vent.overheat_pulse()
                    vent.fade_off()
                    last = 'overheat started'
                    break
                elif near(wand_pulse, 26):
                    #Vent Start (manual or auto)
                    if debug:
                        print('venting started')
                    #SOUNDS HERE
                    vent.vent()
                    vent.idle_pulse()
                    last = 'venting started'
                    break
                elif near(wand_pulse, 32):
                    #Mode Change
                    if debug:
                        print('Mode Changed')
                    mode += 1
                    if debug:
                        print("Mode = " + helpers.mode_decode(mode))
                    #TODO will need to edit cyclotron.py to add sound files
                    cyclotron.mode(mode)
                    last = 'mode change'
                    break
                elif near(wand_pulse, 38):
                    #Song Request
                    if debug:
                        print('playing song')
                    #SONGS HERE
                    last = 'playing song'
                    break
                elif near(wand_pulse, 44):
                    #Intense Fire ON
                    if debug:
                        print('intense fire on')
                    #SOUNDS HERE
                    heating = True
                    vent.heat_up(heating)
                    last = 'intense fire on'
                    break
                elif near(wand_pulse, 50):
                    #Intense Fire OFF
                    if debug:
                        print('Intense fire off')
                    #SOUNDS HERE
                    heating = False
                    vent.cool_down(heating)
                    last = 'intense fire off'
                    break
                elif near(wand_pulse, 56):
                    #Power Down with sound
                    if debug:
                        print('power down (with sound)')
                    #SOUNDS HERE
                    if last != 'power down':
                        bgsound.stopbg()
                        sound = Sound("/root/sounds/power_down_2.wav")
                        sound.play()
                    if cyclotron is not None:
                        cyclotron.fade_off(mode)
                    if statusleds is not None:
                        statusleds.fade_off()
                    if vent is not None:
                        vent.fade_off()
                    cyclotron = None
                    statusleds = None
                    vent = None
                    mode = 0
                    last = 'power down'
                    break
                wand_pulse_val = None
            else:
                if debug:
                    print('wand_pulse_val is None')

def near(number, ideal):
    return abs(number - ideal) <= 3

try:
    main()
except Exception as exception:
    exFile = open(errorLog, "a")
    if wand_pulse_val is not None:
        exFile.write("wand_pulse: " + str(wand_pulse_val // 1000) + "\r\n")
    else:
        exFile.write("wand_pulse_val is None")
    exFile.write("mode: " + str(mode) + "\r\n")
    exFile.write("heating: " + str(heating) + "\r\n")
    exFile.write("error: \r\n" + str(exception) + "\r\n")
    exFile.close()
    sound = Sound("/root/sounds/proton_trap_full.wav")
    sound.play()

