"""
Module to define the Response class and related classes
"""
import time
from typing import ClassVar, Set, List
from dataclasses import dataclass

from application.comm.Common import CommonArgs, CommonComm
from application.trade.ArgTypes import ResponseType, ChildResponseType
from application.trade.Order import Order


class ResponseArgs(CommonArgs):
    """
    Arguments appearing in the order response
    """
    RESPONSE_TYPE = 'ResponseType'
    ERROR_CODE = 'ErrorCode'
    EXCHANGE_ORDER_ID = 'Exchange_Order_Id'
    CHILD_RESPONSE_TYPE = 'ChildResponseType'
    EXCHANGE_TS = 'ExchTs'
    ACCOUNT_ID = 'AccountID'


@dataclass
class Response(CommonComm):
    """
    Response class to handle and send response
    """
    response_type: ResponseType
    error_code: int
    exchange_order_id: int
    child_response_type: ChildResponseType
    exchange_ts: int
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

    @property
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
            value = self.response_dict[arg]
            response += f"{arg}:{value}|"

        response = response[:-1]

        return response

    @classmethod
    def generate_response(cls, order: Order, response_types: Set[ResponseType]) -> List["Response"]:
        responses = list()

        for a_response_type in response_types:
            time_stamp = time.time_ns()
            a_response = cls(
                response_type=a_response_type,
                order_id=order.order_id,
                symbol=order.symbol,
                side=order.side,
                price=order.price,
                quantity=order.quantity,
                account=order.account,
                error_code=cls.get_error(order, a_response_type),
                time_stamp=time_stamp,
                exchange_order_id=cls.get_exchange_order_id(order, a_response_type),
                child_response_type=cls.get_child_response(order, a_response_type),
                duration=order.duration,
                exchange_ts=time_stamp
            )
            responses.append(a_response)

        return responses

    @staticmethod
    def get_error(order: Order, response_type: ResponseType):
        return 1 if response_type != ResponseType.REJECT else 100109

    @staticmethod
    def get_exchange_order_id(order: Order, response_type: ResponseType):
        return 0 if response_type == ResponseType.REJECT else 13007294

    @staticmethod
    def get_child_response(order: Order, response_type: ResponseType):
        if response_type == ResponseType.REJECT:
            return ChildResponseType.CANCEL_ORDER_REJECT_MIDDLE
        else:
            return ChildResponseType.NULL_RESPONSE_MIDDLE
