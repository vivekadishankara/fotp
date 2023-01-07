from application.comm.Request import Request

EXAMPLE_REQUEST = "RequestType:NEWORDER|OrderID:480069891|Token:0|Symbol:IFEU_BRN" \
                  "FMZ0022!|Side:B|Price:157.40000000000000568|Quantity:5|QuantityFilled:0" \
                  "|DisclosedQnty:5|TimeStamp:1666287639395048969|Duration:DAY|OrderType:LIMIT|" \
                  "Account:bJEROM|Exchange:0|NumCopies:0"


class TestRequest:
    def test_parse(self, request_obj):
        assert Request.parse(EXAMPLE_REQUEST) == request_obj

