import threading
import time
import gpiozero
import colorzero
import helpers
import random

class Shooting:

    def __init__(self, spin_speed, heating, status):
        self.spin_speed = spin_speed
        self.heating = heating
        self.status = status

        self.firingMode = gpiozero.Button(22)
        self.firingMode.when_held = None
        self.firingMode.when_pressed = self.firingOn
        self.firingMode.when_released = self.firingOff

        self.canFire = self.firingMode.is_pressed

        self.fireButton = gpiozero.Button(27)
        self.fireButton.hold_time = 0.5

    def firingOn(self):
        self.canFire = True
        sound = Sound("sounds/ai_protongun_powerup.wav")
        sound.play()


    def firingOff(self):
        self.canFire = False
        sound = Sound("sounds/protongun_shutdown.wav")
        sound.play()
    

    #def startFiring(self):
    #    if self.canFire:


    #def stopFiring(self):
