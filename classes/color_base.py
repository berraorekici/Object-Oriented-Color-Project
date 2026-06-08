from abc import ABC, abstractmethod

class InvalidColorValueError(Exception):
    def __init__(self, message="Color value must be between 0 and 255!"):
        self.message = message
        super().__init__(self.message)

class Color(ABC):
    def __init__(self, color_name: str):
        self._color_name = color_name  

    def get_color_name(self) -> str:
        return self._color_name  

    @abstractmethod
    def display_info(self) -> None:
        pass