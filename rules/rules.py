"""
This module needs to be defined by the user. It needs to be in a language that is
more palatable to the user but python is used here as a replacement
"""
from typing import List

from application.trade.Order import Order
from application.trade.ArgTypes import *


def rule_123(order: Order) -> List[ResponseType]:
    """
    If the qty of an order is multiple of x then generate NEW_ORDER_CONFIRM otherwise reject
    """
    if order.quantity % 5 == 0:
        return [ResponseType.NEW_ORDER_CONFIRM]
    else:
        return [ResponseType.REJECT]


def rule_124(order: Order) -> List[ResponseType]:
    """
    If the symbol is xyz then generate new_order_confirm and trade_confirm
    """
    if order.symbol == "IFEU_BRNFMZ0022!":
        return [ResponseType.NEW_ORDER_CONFIRM, ResponseType.TRADE_CONFIRM]


def rule_125(order: Order) -> List[ResponseType]:
    """
    If price is greater than x for symbol xyz then reject
    """
    if order.price > Price(160.0) and order.symbol == "IFEU_BRNFMZ0022!":
        return [ResponseType.REJECT]


def rule_126(order: Order) -> List[ResponseType]:
    """
    If price is 123 then generate reject
    """
    if order.price == Price(123.0):
        return [ResponseType.REJECT]
