# Object-Oriented Color Management Project

This is a Python project for my Object-Oriented Programming (OOP) course. It manages colors and palettes using OOP principles and a sorting algorithm.

## OOP Principles Used

* **Abstraction:** Created an abstract base class named `Color`.
* **Inheritance:** `RGBColor` class inherits from the `Color` class.
* **Encapsulation:** Protected color attributes and used getters/setters to access them safely.
* **Custom Exception:** Created `InvalidColorValueError` to catch errors if RGB values are not between 0 and 255.
* **Polymorphism:** The `Palette` class can store and handle different color objects together in a list.
* **Sorting Algorithm:** Implemented a custom **Bubble Sort** algorithm to sort colors by their Red value.

## Project Structure

* `classes/` - Contains all OOP classes (`color_base.py`, `rgb_color.py`, `palette.py`).
* `tests/` - Contains unit tests for testing the code.
* `main.py` - The main file that runs the project and demonstrates how it works.

---
**Author:** Berra Orekici
