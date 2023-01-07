"""
Module to define types for trade values used throughout the application
"""
from application.utils.BaseTypes import AppFloat, BaseEnum


class Price(AppFloat):
    """
    Class to represent prices for the orders
    """


class RequestType(BaseEnum):
    NEW_ORDER = 'NEWORDER'


class ResponseType(BaseEnum):
    NEW_ORDER_CONFIRM = 'NEW_ORDER_CONFIRM'
    TRADE_CONFIRM = 'TRADE_CONFIRM'
    REJECT = 'REJECT'
