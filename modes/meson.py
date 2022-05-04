from __future__ import annotations
from mode import State
from pygame import mixer
import gpiozero

class Meson(State):

    def __init__(self) -> None:
        """
        Turns off leds to prevent rogue voltage to pins
        """

        self.cyc1.off()
        self.cyc2.off()
        self.cyc3.off()
        self.cyc4.off()

        self.statRed.off()
        self.statYellow.off()
        self.statGreen.off()

        self.fule.off()

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
