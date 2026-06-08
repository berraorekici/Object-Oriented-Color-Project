from classes.color_base import Color, InvalidColorValueError

class RGBColor(Color):
    def __init__(self, color_name: str, r: int, g: int, b: int):
        super().__init__(color_name)
        
        if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
            raise InvalidColorValueError(f"Invalid RGB values ({r}, {g}, {b}) for '{color_name}'. Must be 0-255!")
            
        self._r = r
        self._g = g
        self._b = b

    def display_info(self) -> None:
        print(f"Color Name: {self.get_color_name()} | Type: RGB | Values: (R: {self._r}, G: {self._g}, B: {self._b})")