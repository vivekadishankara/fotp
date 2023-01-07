import pytest

from application.comm.Request import Request
from application.trade.ArgTypes import *

EXAMPLE_REQUEST = "RequestType:NEWORDER|OrderID:480069891|Token:0|Symbol:IFEU_BRN" \
                  "FMZ0022!|Side:B|Price:157.40000000000000568|Quantity:5|QuantityFilled:0" \
                  "|DisclosedQnty:5|TimeStamp:1666287639395048969|Duration:DAY|OrderType:LIMIT|" \
                  "Account:bJEROM|Exchange:0|NumCopies:0"


class TestRequest:
    @pytest.fixture
    def request_obj(self):
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

    def test_parse(self, request_obj):
        assert Request.parse(EXAMPLE_REQUEST) == request_obj

