# https://auth0.com/blog/state-pattern-in-python/
from __future__ import annotations
from abc import ABC, abstractmethod
from mode import State
from off import Off
from pygame import mixer
import gpiozero

from ../background import Background
from ../cyclotron import Cyclotron
from ../status import FiringStatusLeds
from ../vent import Vent

class Pack:

    _state = None
    _previous = Off()

    def __init__(self, state: State) -> None:
        self.setState(state)

        # sets up all classes
        self.background = Background()
        self.cyclotron = Cyclotron()
        self.statusleds = FiringStatusLeds()
        self.vent = Vent()

    def setState(self, state: State):
        self._state = state
        self._state.pack = self

    def currentState(self):
        print(f"The proton pack is in {type(self._state).__name__} mode")

    def arm(self):
        self._state.arm()

    def disarm(self):
        self._state.disarm()

    def fire(self):
        self._state.fire()

    def ceasefire(self):
        self._state.ceasefire()


    def exitState(self):
        self._state.exitState()

    def  packOff(self):
        self._state.packOff()
        self.setState(Off())

    #TODO check if mode stays same after disarm
