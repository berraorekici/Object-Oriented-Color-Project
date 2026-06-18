from classes.color_base import Color
from classes.rgb_color import RGBColor


class HexColor(Color):
    def __init__(self, hex_code):
        if not isinstance(hex_code, str):
            raise ValueError("Hex code must be a string")

        if hex_code.startswith("#"):
            hex_code = hex_code[1:]

        if len(hex_code) != 6:
            raise ValueError("Hex code must have 6 characters")

        self._hex_code = hex_code.upper()

    def to_rgb(self):
        r = int(self._hex_code[0:2], 16)
        g = int(self._hex_code[2:4], 16)
        b = int(self._hex_code[4:6], 16)
        return r, g, b

    def brightness(self):
        r, g, b = self.to_rgb()
        return (r + g + b) / 3

    def invert(self):
        r, g, b = self.to_rgb()
        return RGBColor(255 - r, 255 - g, 255 - b)

    def __str__(self):
        return f"HEX(#{self._hex_code})"