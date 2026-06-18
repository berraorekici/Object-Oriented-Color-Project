# Object-Oriented Color Management Project

This is a Python project for my Object-Oriented Programming (OOP) course. The project manages different color types and color palettes using OOP principles.

## OOP Principles Used

### Abstraction

I created an abstract base class called `Color`.

### Inheritance

The following classes inherit from `Color`:

* `RGBColor`
* `HexColor`
* `CMYKColor`

### Encapsulation

Color values are stored as protected attributes and validated before use.

### Polymorphism

The `Color` class defines abstract methods:

* `to_rgb()`
* `brightness()`
* `invert()`

Each subclass implements these methods differently.

The `Palette` class works with `Color` objects without knowing their exact type. It can store `RGBColor`, `HexColor`, and `CMYKColor` objects together and use the same methods on all of them.

### Exception Handling

The project checks for invalid color values and raises exceptions when necessary.

## Project Structure

* `classes/` - Contains all class definitions.
* `tests/` - Contains unit tests.
* `main.py` - Demonstrates the project features.

## Testing

The project includes unit tests using Python's `unittest` module.

The tests check:

* RGB to RGB conversion
* HEX to RGB conversion
* CMYK to RGB conversion
* Invalid RGB values
* Palette support for different color types

## Example Class Hierarchy

Color (Abstract Class)

* RGBColor
* HexColor
* CMYKColor

---

**Author:** Berra Orekici
