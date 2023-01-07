
EXAMPLE_RESPONSE = "ResponseType:NEW_ORDER_CONFIRM|OrderID:480069891|Symbol:IFEU_BRN" \
                   "FMZ0022!|Side:B|Price:157.40000000000000568|Quantity:5|AccountID:bJEROM" \
                   "|ErrorCode:1|TimeStamp:1666287639692625876|Exchange_Order_Id:13007294|" \
                   "ChildResponseType:NULL_RESPONSE_MIDDLE|Duration:DAY|ExchTs:1666287639962000000"


class TestResponse:
    def test_build_response(self, response):
        assert response.build_response() == EXAMPLE_RESPONSE
