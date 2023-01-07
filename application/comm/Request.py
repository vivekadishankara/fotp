"""
Module to define the Request class and other related classes
"""
from dataclasses import dataclass

from application.comm.Common import CommonArgs, CommonComm


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
    request_type: str
    token: int
    quantity_filled: int
    disclosed_quantity: int
    order_type: str
    exchange: int
    num_copies: int

    @staticmethod
    def parse(request_string: str) -> dict:
        """
        Parse and oder string that is accompanies an order file
        :param request_string: string read from an order file
        :return: dict
        """
        request_list = request_string.split('|')
        request_dict = {}
        for entry in request_list:
            arg, value = entry.split(':')
            request_dict[arg] = value

        return request_dict

    def look_for_order(self):
        """
        look for new orders in the 'requests' folder
        :return:
        """
        pass

