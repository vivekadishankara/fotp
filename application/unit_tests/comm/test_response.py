import pytest
from application.comm.Response import Response


EXAMPLE_RESPONSE = "ResponseType:NEW_ORDER_CONFIRM|OrderID:480069891|Symbol:IFEU_BRN" \
                   "FMZ0022!|Side:B|Price:157.40000000000000568|Quantity:5|AccountID:bJEROM" \
                   "|ErrorCode:1|TimeStamp:1666287639692625876|Exchange_Order_Id:13007294|" \
                   "ChildResponseType:NULL_RESPONSE_MIDDLE|Duration:DAY|ExchTs:1666287639962000000"


class TestResponse:
    @pytest.fixture
    def response(self):
        return Response(response_type="NEW_ORDER_CONFIRM",
                        order_id=480069891,
                        symbol="IFEU_BRNFMZ0022!",
                        side="B",
                        price=157.40000000000000568,
                        quantity=5,
                        account="bJEROM",
                        error_code=1,
                        time_stamp=1666287639692625876,
                        exchange_order_id=13007294,
                        child_response_type="NULL_RESPONSE_MIDDLE",
                        duration="DAY",
                        exchange_ts=1666287639962000000)

    def test_build_response(self, response):
        assert response.build_response() == EXAMPLE_RESPONSE
