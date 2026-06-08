import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.rgb_color import RGBColor

print("=== RGBColor Isolated Test ===")
test_green = RGBColor("Test Green", 0, 255, 0)
test_green.display_info()