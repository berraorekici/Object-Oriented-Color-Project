from classes.color_base import Color


class Palette:
    def __init__(self, name):
        self._name = name
        self._colors = []

    def add_color(self, color):
        if not isinstance(color, Color):
            raise TypeError("Only Color objects can be added")
        self._colors.append(color)

    def sort_by_brightness(self):
        self._colors.sort(key=lambda color: color.brightness())

    def invert_all(self):
        inverted_palette = Palette(self._name + " inverted")

        for color in self._colors:
            inverted_palette.add_color(color.invert())

        return inverted_palette

    def get_rgb_values(self):
        return [color.to_rgb() for color in self._colors]

    def __str__(self):
        result = f"Palette: {self._name}\n"
        for color in self._colors:
            result += f"{color} | RGB: {color.to_rgb()} | Brightness: {color.brightness()}\n"
        return result