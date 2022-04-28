from __future__ import annotations
from mode import State
from pygame import mixer
import gpiozero

class Off(State):

    def __init__(self) -> None:
        """
        Sets up leds to prevent pin bleed
        """

        self.cyc1 = gpiozero.RGBLED(0,1,2)
        self.cyc2 = gpiozero.RGBLED(3,4,5)
        self.cyc3 = gpiozero.RGBLED(6,7,8)
        self.cyc4 = gpiozero.RGBLED(9,10,11)

        self.statRed = gpiozero.PWMLED(15)
        self.statYellow = gpiozero.PWMLED(16)
        self.statGreen = gpiozero.PWMLED(17)

        self.fule = gpiozero.RGBLED(13,19,26)

    def arm(self) -> None:
        pass

    def disarm(self) -> None:
        pass

    def fire(self) -> None:
        pass

    def ceasefire(self) -> None:
        pass

    def exitState(self) -> None:
        """
        Turns proton pack on.
        """

        sound = mixer.Sound("../sounds/protongun_powerup.wav")
        sound.play()

        self.context.setState(On())

    def packOff(self) -> None:
        pass
