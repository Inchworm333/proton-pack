import threading
import time
import gpiozero
import colorzero
from sound_player import Sound, Playlist, SoundPlayer
import helpers
import random

class Shooting:

    def __init__(self, spin_speed, heating, status):
        self.spin_speed = spin_speed
        self.heating = heating
        self.status = status

        self.firingMode = gpiozero.Button(22, False)
        self.firingMode.when_pressed = self.firingOn
        self.firingMode.when_released = self.firingOff

        self.canFire = self.firingMode.is_pressed

        self.fireButton = gpiozero.Button(27, False)
        self.fireButton.hold_time = 0.5
        self.fireButton.when_held = self.testbutton

    def firingOn(self):
        print("firing on")
        sound = Sound("sounds/ai_protongun_powerup.wav")
        sound.play()
        self.canFire = True


    def firingOff(self):
        print("firing off")
        sound = Sound("sounds/protongun_shutdown.wav")
        sound.play()
        self.canFire = False


    def testbutton(self):
        print("I am a button")
    

    #def startFiring(self):
    #    if self.canFire:


    #def stopFiring(self):
