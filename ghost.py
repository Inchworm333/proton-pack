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
from status import FiringStatusLeds

#SHOOTING MODE VARIABLE
mode = 0

def main():
 
    PWM_GPIO = 12 #TODO: find better gpio
    PWM_RUN_TIME = 60.0
    PWM_SAMPLE_TIME = 2.0

    #cyclotron
    cyclotron = Cyclotron()
    statusleds = FiringStatusLeds()
    while True:
        None

main()


