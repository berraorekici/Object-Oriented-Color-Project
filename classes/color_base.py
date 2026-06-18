from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def to_rgb(self):
        pass

    @abstractmethod
    def brightness(self):
        pass

    @abstractmethod
    def invert(self):
        pass