"""
Concrete CottageBuilder class that inherits AbstractBuilder.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""
from creational.builder.house_builder.abstract_builder import AbstractBuilder

from creational.builder.house_parts.door import Door
from creational.builder.house_parts.roof import Roof
from creational.builder.house_parts.window import Window


class CottageBuilder(AbstractBuilder):
    """CottageBuilder class with implementation for abstract methods.

    In this class, we provide implementation for each abstract
    method we defined in AbstractBuilder class.
    """
    def __init__(self):
        self.build_type = "Cottage"

    def get_door(self):
        door_obj = Door(6)
        return door_obj.door

    def get_roof(self):
        # Is there such a thing as Green Roof?
        # Yes, there is!
        roof_obj = Roof("Green Roof")
        return roof_obj.roof

    def get_window(self):
        window_obj = Window(4)
        return window_obj.window


if __name__ == "__main__":
    # Checking if CottageBuilder works!
    cottage_obj = CottageBuilder()
    print(cottage_obj)

