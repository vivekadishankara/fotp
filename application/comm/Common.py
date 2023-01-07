"""
Common Args class is defined here
"""
from typing import Union
from dataclasses import dataclass

from application.trade.ArgTypes import Price


class CommonArgs:
    """
    Common arguments that appear in the request and response
    """
    ORDERID = 'OrderID'
    SYMBOL = 'Symbol'
    SIDE = 'Side'
    PRICE = 'Price'
    QUANTITY = 'Quantity'
    TIME_STAMP = 'TimeStamp'
    DURATION = 'Duration'


@dataclass
class CommonComm:
    order_id: int
    symbol: str
    side: str
    price: Union[Price, float]
    quantity: int
    time_stamp: int
    duration: str
    account: str

    def __post_init__(self):
        if isinstance(self.price, float):
            self.price = Price(self.price)
