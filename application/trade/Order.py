"""
Module to define the Trade class and other related classes
"""
from application.comm.Request import Request


class Order:
    def __init__(self, request: Request):
        self.request = request

    def __getattr__(self, item):
        return getattr(self.request, item)



