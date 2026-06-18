from classes.color_base import Color
from classes.rgb_color import RGBColor


class CMYKColor(Color):
    def __init__(self, c, m, y, k):
        values = [c, m, y, k]

        for value in values:
            if not (0 <= value <= 100):
                raise ValueError("CMYK values must be between 0 and 100")

        self._c = c
        self._m = m
        self._y = y
        self._k = k

    def to_rgb(self):
        r = 255 * (1 - self._c / 100) * (1 - self._k / 100)
        g = 255 * (1 - self._m / 100) * (1 - self._k / 100)
        b = 255 * (1 - self._y / 100) * (1 - self._k / 100)

        return int(r), int(g), int(b)

    def brightness(self):
        r, g, b = self.to_rgb()
        return (r + g + b) / 3

    def invert(self):
        r, g, b = self.to_rgb()
        return RGBColor(255 - r, 255 - g, 255 - b)

    def __str__(self):
        return f"CMYK({self._c}, {self._m}, {self._y}, {self._k})"