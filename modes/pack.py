# https://auth0.com/blog/state-pattern-in-python/
from __future__ import annotations
from abc import ABC, abstractmethod

class Pack:

    _stat = None

    def __init__(self, state: State) -> None:
        self.setPack(state)

    def setPack(self, state: State):
        self._state = state
        self._state.pack = self

    def currentState(self):
        print(f"The proton pack is in {type(self._state).__name__} mode")
