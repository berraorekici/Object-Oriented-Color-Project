from classes.rgb_color import RGBColor
from classes.palette import Palette

print("--- Running MAIN Program with Sorting Feature ---")

art_palette = Palette("Masterpiece Studio")

print("\n[Action] Creating colors with different Red values...")
low_red = RGBColor("Ocean Blue", 10, 150, 255)       
mid_red = RGBColor("Emerald Green", 120, 220, 110)  
high_red = RGBColor("Fire Red", 255, 20, 40)        

art_palette.add_color(low_red)
art_palette.add_color(high_red)
art_palette.add_color(mid_red)

print("\nBefore Sorting:")
art_palette.show_palette()

art_palette.sort_by_red_intensity()

print("\nAfter Sorting (Highest Red to Lowest Red):")
art_palette.show_palette()

print("\n--- Project Fully Completed Successfully! ---")