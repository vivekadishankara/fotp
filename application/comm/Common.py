"""
Common Args class is defined here
"""
from dataclasses import dataclass


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
    price: float
    quantity: int
    time_stamp: str
    duration: str
    account: str
