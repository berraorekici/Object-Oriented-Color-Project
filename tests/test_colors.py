import unittest

from classes.rgb_color import RGBColor
from classes.hex_color import HexColor
from classes.cmyk_color import CMYKColor
from classes.palette import Palette


class TestColors(unittest.TestCase):

    def test_rgb_to_rgb(self):
        color = RGBColor(255, 0, 0)
        self.assertEqual(color.to_rgb(), (255, 0, 0))

    def test_hex_to_rgb(self):
        color = HexColor("#00FF00")
        self.assertEqual(color.to_rgb(), (0, 255, 0))

    def test_cmyk_to_rgb(self):
        color = CMYKColor(100, 0, 0, 0)
        self.assertEqual(color.to_rgb(), (0, 255, 255))

    def test_invalid_rgb(self):
        with self.assertRaises(ValueError):
            RGBColor(300, 0, 0)

    def test_palette_accepts_different_color_types(self):
        palette = Palette("Test")
        palette.add_color(RGBColor(255, 0, 0))
        palette.add_color(HexColor("#00FF00"))
        palette.add_color(CMYKColor(100, 0, 0, 0))

        self.assertEqual(len(palette.get_rgb_values()), 3)


if __name__ == "__main__":
    unittest.main()