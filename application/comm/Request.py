"""
Module to define the Request class and other related classes
"""
from dataclasses import dataclass
from typing import ClassVar

from application.comm.Common import CommonArgs, CommonComm
from application.trade.ArgTypes import *


class RequestArgs(CommonArgs):
    """
    Arguments appearing in the order request
    """
    REQUEST_TYPE = 'RequestType'
    TOKEN = 'Token'
    QUANTITY_FILLED = 'QuantityFilled'
    DISCLOSED_QUANTITY = 'DisclosedQnty'
    ORDER_TYPE = 'OrderType'
    EXCHANGE = 'Exchange'
    NUM_COPIES = 'NumCopies'
    ACCOUNT = 'Account'


@dataclass
class Request(CommonComm):
    """
    Represents the Order request
    """
    request_type: RequestType
    token: int
    quantity_filled: int
    disclosed_quantity: int
    order_type: OrderType
    exchange: int
    num_copies: int
    ARG_VAR_NAME: ClassVar[dict] = {
        RequestArgs.REQUEST_TYPE: 'request_type',
        RequestArgs.ORDERID: 'order_id',
        RequestArgs.TOKEN: 'token',
        RequestArgs.SYMBOL: 'symbol',
        RequestArgs.SIDE: 'side',
        RequestArgs.PRICE: 'price',
        RequestArgs.QUANTITY: 'quantity',
        RequestArgs.QUANTITY_FILLED: 'quantity_filled',
        RequestArgs.DISCLOSED_QUANTITY: 'disclosed_quantity',
        RequestArgs.TIME_STAMP: 'time_stamp',
        RequestArgs.DURATION: 'duration',
        RequestArgs.ORDER_TYPE: 'order_type',
        RequestArgs.ACCOUNT: 'account',
        RequestArgs.EXCHANGE: 'exchange',
        RequestArgs.NUM_COPIES: 'num_copies',
    }
    INT_ARGS: ClassVar[list] = [
        RequestArgs.ORDERID,
        RequestArgs.QUANTITY,
        RequestArgs.TOKEN,
        RequestArgs.TIME_STAMP,
        RequestArgs.QUANTITY_FILLED,
        RequestArgs.DISCLOSED_QUANTITY,
        RequestArgs.EXCHANGE,
        RequestArgs.NUM_COPIES
    ]

    @classmethod
    def parse(cls, request_string: str) -> "Request":
        """
        Parse and oder string that is accompanies an order file
        :param request_string: string read from an order file
        :return: dict
        """
        request_list = request_string.split('|')
        request_dict = {}
        for entry in request_list:
            arg, value = entry.split(':')
            if arg == RequestArgs.REQUEST_TYPE:
                value = RequestType(value)
            elif arg == RequestArgs.SIDE:
                value = Side(value)
            elif arg == RequestArgs.DURATION:
                value = Duration(value)
            elif arg == RequestArgs.ORDER_TYPE:
                value = OrderType(value)
            elif arg == RequestArgs.PRICE:
                value = Price(value)
            elif arg in cls.INT_ARGS:
                value = int(value)
            request_dict[cls.ARG_VAR_NAME[arg]] = value

        return cls(**request_dict)

    def look_for_order(self):
        """
        look for new orders in the 'requests' folder
        :return:
        """
        pass

