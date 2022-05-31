from __future__ import annotations
from abc import ABC, abstractmethod
from pack import Pack

class State(ABC):
    @property
    def context(self) -> Pack:
        return self._pack

    @property
    def previous(self) -> State:
        return self.context._previous

    @context.setter
    def context(self, pack: Pack) -> None:
        self._pack = pack

    @previous.setter
    def previous(self, previous: State) -> None:
        self.context._previous = previous

    @abstractmethod
    def arm(self) -> None:
        pass

    @abstractmethod
    def disarm(self) -> None:
        pass

    @abstractmethod
    def fire(self) -> None:
        pass

    @abstractmethod
    def ceasefire(self) -> None:
        pass

    @abstractmethod
    def exitState(self) -> None:
        pass

    @abstractmethod
    def packOff(self) -> None:
        pass
