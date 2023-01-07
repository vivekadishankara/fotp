"""
Module to define types for trade values used throughout the application
"""


class AppFloat(float):
    def __str__(self):
        # Assumption: The number of digits after decimal in price is 17
        return "{:.17f}".format(self.real)
