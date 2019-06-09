"""
Door class to build house using Builder design pattern.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""


class Door(object):
    def __init__(self, num_of_door):
        """
        Number of door in the house
        :param num_door:
        """
        self.num_of_door = num_of_door

    @property
    def door(self):
        return self.num_of_door

    @door.setter
    def door(self, value_to_set):
        self.num_of_door = value_to_set


if __name__ == "__main__":
    door_obj = Door(5)
    print(door_obj.door)
