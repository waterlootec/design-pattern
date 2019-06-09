"""
Represents generic House class.

Each House will be built based on builder provided.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""


class House(object):
    def __init__(self):
        self.num_of_door = None
        self.roof_type = None
        self.num_of_window = None
        self.house_type = None

    @property
    def door(self):
        return self.num_of_door

    @door.setter
    def door(self, door_value):
        self.num_of_door = door_value

    @property
    def roof(self):
        return self.roof_type

    @roof.setter
    def roof(self, roof_value):
        self.roof_type = roof_value

    @property
    def window(self):
        return self.num_of_window

    @window.setter
    def window(self, window_value):
        self.num_of_window = window_value

    @property
    def build(self):
        return self.house_type

    @build.setter
    def build(self, build_value):
        self.house_type = build_value

    def show_house(self):
        title = 'House Build Info'
        print("\n{}{}{}".format("="*20, title, "="*20))

        print(self.build)
        print("door={}, roof={}, window={}".format(
            self.door, self.roof, self.window))

        print("{}".format("=" * int(20*2+len(title))))


if __name__ == "__main__":
    # Test our House class individually
    house = House()
    house.door = 9
    house.roof = "Green Roof"
    house.window = 4
    house.build = "Cottage"
    house.show_house()

