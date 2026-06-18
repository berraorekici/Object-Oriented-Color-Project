from classes.color_base import Color


class RGBColor(Color):
    def __init__(self, r, g, b):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be between 0 and 255")

        self._r = r
        self._g = g
        self._b = b

    def to_rgb(self):
        return self._r, self._g, self._b

    def brightness(self):
        return (self._r + self._g + self._b) / 3

    def invert(self):
        return RGBColor(255 - self._r, 255 - self._g, 255 - self._b)

    def __str__(self):
        return f"RGB({self._r}, {self._g}, {self._b})"