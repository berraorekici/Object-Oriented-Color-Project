from classes.color_base import Color
from classes.rgb_color import RGBColor

class Palette:
    def __init__(self, palette_name: str):
        self._palette_name = palette_name
        self._colors = []

    def add_color(self, color: Color) -> None:
        if isinstance(color, Color):
            self._colors.append(color)
            print(f"🎨 [Palette] Added '{color.get_color_name()}' to the palette '{self._palette_name}'.")
        else:
            print("❌ [Palette Error] Only objects derived from Color class can be added!")

    def show_palette(self) -> None:
        print(f"\n=== Displaying Palette: {self._palette_name} ===")
        if not self._colors:
            print("The palette is currently empty.")
            return
        for color in self._colors:
            color.display_info()
        print("=======================================")

    def sort_by_red_intensity(self) -> None:
        n = len(self._colors)
        if n <= 1:
            return  

        print(f"\n🔄 [Sorting] Sorting palette '{self._palette_name}' by Red (R) intensity (Highest to Lowest)...")
        
        for i in range(n):
            for j in range(0, n - i - 1):
                color1 = self._colors[j]
                color2 = self._colors[j + 1]
                
                if isinstance(color1, RGBColor) and isinstance(color2, RGBColor):
                    if color1._r < color2._r:
                        self._colors[j], self._colors[j + 1] = self._colors[j + 1], self._colors[j]
                        
        print("✅ [Sorting] Sorting completed successfully!")