"""
Module to define the Response class and related classes
"""
from typing import ClassVar
from dataclasses import dataclass

from application.comm.Common import CommonArgs, CommonComm


class ResponseArgs(CommonArgs):
    """
    Arguments appearing in the order response
    """
    RESPONSE_TYPE = 'ResponseType'
    ERROR_CODE = 'ErrorCode'
    EXCHANGE_ORDER_ID = 'Exchange_Oder_Id'
    CHILD_RESPONSE_TYPE = 'ChildResponseType'
    EXCHANGE_TS = 'ExchangeTs'
    ACCOUNT_ID = 'AccountID'


@dataclass
class Response(CommonComm):
    """
    Response class to handle and send response
    """
    response_type: str
    error_code: int
    exchange_order_id: int
    child_response_type: str
    exchange_ts: str
    # this solution to add class variable to dataclass was found here:
    # https://stackoverflow.com/questions/67955425/
    #   how-to-add-the-class-instance-to-a-class-variable-in-dataclass-notation
    ARG_ORDER: ClassVar[list] = [
        ResponseArgs.RESPONSE_TYPE,
        ResponseArgs.ORDERID,
        ResponseArgs.SYMBOL,
        ResponseArgs.SIDE,
        ResponseArgs.PRICE,
        ResponseArgs.QUANTITY,
        ResponseArgs.ACCOUNT_ID,
        ResponseArgs.ERROR_CODE,
        ResponseArgs.TIME_STAMP,
        ResponseArgs.EXCHANGE_ORDER_ID,
        ResponseArgs.CHILD_RESPONSE_TYPE,
        ResponseArgs.DURATION,
        ResponseArgs.EXCHANGE_TS
    ]

    def response_dict(self) -> dict:
        """
        Create a dictionary of response args and the corresponding values
        :return: dict
        """
        response_dict = dict()

        response_dict[ResponseArgs.RESPONSE_TYPE] = self.response_type
        response_dict[ResponseArgs.ORDERID] = self.order_id
        response_dict[ResponseArgs.SYMBOL] = self.symbol
        response_dict[ResponseArgs.SIDE] = self.side
        response_dict[ResponseArgs.PRICE] = self.price
        response_dict[ResponseArgs.QUANTITY] = self.quantity
        response_dict[ResponseArgs.ACCOUNT_ID] = self.account
        response_dict[ResponseArgs.ERROR_CODE] = self.error_code
        response_dict[ResponseArgs.TIME_STAMP] = self.time_stamp
        response_dict[ResponseArgs.EXCHANGE_ORDER_ID] = self.exchange_order_id
        response_dict[ResponseArgs.CHILD_RESPONSE_TYPE] = self.child_response_type
        response_dict[ResponseArgs.DURATION] = self.duration
        response_dict[ResponseArgs.EXCHANGE_TS] = self.exchange_ts

        return response_dict

    def build_response(self):
        response = ''
        for arg in self.ARG_ORDER:
            pass

