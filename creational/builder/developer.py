"""
Represent a real estate developer who builds different houses.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""

from creational.builder.house import House


class Developer(object):
    def __init__(self, house_builder):
        self.builder = house_builder

    def build_house(self):
        house = House()
        house.door = self.builder.get_door()
        house.roof = self.builder.get_roof()
        house.window = self.builder.get_window()
        house.build = self.builder.build_type
        return house


if __name__ == "__main__":
    pass
