from abc import ABC, abstractmethod
class Color(ABC):
    def __init__(self, color_name: str):
        self._color_name = color_name
    def get_color_name(self) -> str:
        return self._color_name
    @abstractmethod
    def display_info(self):
        pass

class RGBColor(Color):
    def __init__(self, color_name: str, r: int, g: int, b: int):
        super().__init__(color_name)

        self._r = r
        self._g = g
        self._b = b

    def display_info(self):
        print(f"Color Name: {self.get_color_name()} | Type: RGB | Values: (R: {self._r}, G: {self._g}, B: {self._b})")

red_color = RGBColor("Fire Red", 255, 0, 0)
blue_color = RGBColor("Ocean Blue", 0, 0, 255)

print("--- Running Color Test ---")
red_color.display_info()
blue_color.display_info()