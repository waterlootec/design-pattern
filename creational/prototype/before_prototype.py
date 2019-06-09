"""
Demonstrates problem statement to build the case for Prototype pattern.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""


class House(object):
    def __init__(self):
        pass

    def __repr__(self):
        """Print object attributes.

        This is a quick way to print object attributes.
        It is not ideal to use __repr__ this way but
        we use it this way for convenience.

        :return:
        """
        return str(self.__dict__)


class DuplexHouse(House):
    def __init__(self, door, window):
        super(DuplexHouse, self).__init__()
        self.door = door
        self.window = window


class KonakHouse(House):
    def __init__(self, door, window, pool):
        super(KonakHouse, self).__init__()
        self.door = door
        self.window = window
        self.pool = pool


if __name__ == "__main__":
    house = House()
    print(house)

    dup = DuplexHouse(13, 9)
    print(dup)

    konak = KonakHouse(50, 100, 2)
    print(konak)



