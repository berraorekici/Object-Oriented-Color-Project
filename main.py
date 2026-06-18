from classes.rgb_color import RGBColor
from classes.hex_color import HexColor
from classes.cmyk_color import CMYKColor
from classes.palette import Palette


palette = Palette("My Color Palette")

palette.add_color(RGBColor(255, 0, 0))
palette.add_color(HexColor("#00FF00"))
palette.add_color(CMYKColor(100, 0, 0, 0))

print("Original palette:")
print(palette)

palette.sort_by_brightness()

print("Sorted by brightness:")
print(palette)

inverted = palette.invert_all()

print("Inverted palette:")
print(inverted)