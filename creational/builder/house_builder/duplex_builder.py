"""
Concrete DuplexBuilder class that inherits AbstractBuilder.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""
from creational.builder.house_builder.abstract_builder import AbstractBuilder

from creational.builder.house_parts.door import Door
from creational.builder.house_parts.roof import Roof
from creational.builder.house_parts.window import Window


class DuplexBuilder(AbstractBuilder):
    """DuplexBuilder class with implementation for abstract methods.

    In this class, we provide implementation for each abstract
    method we defined in AbstractBuilder class. Notice how each
    type of concrete house builder is constructed is different ways.
    For an example, roof type, number of door, and number of window
    varies between CottageBuilder and DuplexBuilder.
    """
    def __init__(self):
        self.build_type = "Duplex"

    def get_door(self):
        door_obj = Door(12)
        return door_obj.door

    def get_roof(self):
        roof_obj = Roof("Gable Roof")
        return roof_obj.roof

    def get_window(self):
        window_obj = Window(9)
        return window_obj.window


if __name__ == "__main__":
    # Checking if DuplexBuilder works!
    d = DuplexBuilder()
    print(d.get_roof())

