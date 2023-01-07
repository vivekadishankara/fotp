import pytest

from application.comm.Request import Request
from application.comm.Response import Response
from application.trade.ArgTypes import *


@pytest.fixture
def request_obj():
    request = Request(request_type=RequestType.NEW_ORDER,
                      order_id=480069891,
                      token=0,
                      symbol="IFEU_BRNFMZ0022!",
                      side=Side.B,
                      price=157.40000000000000568,
                      quantity=5,
                      quantity_filled=0,
                      disclosed_quantity=5,
                      time_stamp=1666287639395048969,
                      duration=Duration.DAY,
                      order_type=OrderType.LIMIT,
                      account="bJEROM",
                      exchange=0,
                      num_copies=0)
    return request


@pytest.fixture
def response():
    return Response(response_type=ResponseType.NEW_ORDER_CONFIRM,
                    order_id=480069891,
                    symbol="IFEU_BRNFMZ0022!",
                    side=Side.B,
                    price=157.40000000000000568,
                    quantity=5,
                    account="bJEROM",
                    error_code=1,
                    time_stamp=1666287639692625876,
                    exchange_order_id=13007294,
                    child_response_type=ChildResponseType.NULL_RESPONSE_MIDDLE,
                    duration=Duration.DAY,
                    exchange_ts=1666287639962000000)
