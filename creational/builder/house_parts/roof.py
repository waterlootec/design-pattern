"""
Roof class to build house using Builder design pattern.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""


class Roof(object):
    def __init__(self, roof_type):
        """
        Roof type could be Gable, Green Roof, Pyramid.

        :param roof_type:
        """
        self.roof_type = roof_type

    @property
    def roof(self):
        return self.roof_type

    @roof.setter
    def roof(self, value_to_set):
        self.roof_type = value_to_set


if __name__ == "__main__":
    pass
