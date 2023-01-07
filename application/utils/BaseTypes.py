"""
This module defines new types to be used in the application
"""
from enum import Enum


class AppFloat(float):
    def __str__(self):
        # Assumption: The number of digits after decimal in price is 17
        return "{:.17f}".format(self.real)


class BaseEnum(Enum):
    def __str__(self):
        return self.value
