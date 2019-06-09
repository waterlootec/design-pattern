"""
Window class to build house using Builder design pattern.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""


class Window(object):
    def __init__(self, num_of_window):
        self.num_of_window = num_of_window

    @property
    def window(self):
        return self.num_of_window

    @window.setter
    def window(self, value_to_set):
        self.num_of_window = value_to_set


if __name__ == "__main__":
    pass
