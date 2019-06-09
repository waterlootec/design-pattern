"""
Abstract house builder class that defines high-level contract.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
"""

from abc import ABC, abstractmethod


class AbstractBuilder(ABC):
    """House builder abstract class that defines abstraction.

    Note that we do not provide any implementation on purpose.
    Each function is made abstract.

    """
    def __init__(self):
        pass

    @abstractmethod
    def get_door(self):
        pass

    @abstractmethod
    def get_roof(self):
        pass

    @abstractmethod
    def get_window(self):
        pass


if __name__ == "__main__":
    pass
