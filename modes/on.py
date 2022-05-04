from __future__ import annotations
import time
from mode import State
from pygame import mixer
import gpiozero

class On(State):

    def __init__(self) -> None:
        """
        Turn the proton pack on + initiate classes
        """

        sound = mixer.Sound("../sounds/protongun_powerup.wav")
        sound.play()


        time.sleep(3)
        self.background.playbg()

    def arm(self) -> None:
        pass

    def disarm(self) -> None:
        pass

    def fire(self) -> None:
        pass

    def ceasefire(self) -> None:
        pass

    def exitState(self) -> None:
        pass

    def packOff(self) -> None:
        pass
