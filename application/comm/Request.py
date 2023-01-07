from dataclasses import dataclass


class RequestArgs:
    REQUEST_TYPE = 'RequestType'
    ORDERID = 'OrderID'
    TOKEN = 'Token'
    SYMBOL = 'Symbol'
    SIDE = 'Side'
    PRICE = 'Price'
    QUANTITY = 'Quantity'
    QUANTITY_FILLED = 'QuantityFilled'
    DISCLOSED_QUANTITY = 'DisclosedQnty'
    TIME_STAMP = 'TimeStamp'
    DURATION = 'Duration'
    ORDER_TYPE = 'OrderType'
    ACCOUNT = 'Account'
    EXCHANGE = 'Exchange'
    NUM_COPIES = 'NumCopies'


@dataclass(frozen=True)
class Request:
    request_type: str
    order_id: int
    token: int
    symbol: str
    side: str
    price: float
    quantity: int
    quantity_filled: int
    disclosed_quantity: int
    time_stamp: int
    duration: str
    order_type: str
    account: str
    exchange: int
    num_copies: int

    @staticmethod
    def parse(request_string):
        request_list = request_string.split('|')
        request_dict = {}
        for entry in request_list:
            arg, value = entry.split(':')
            request_dict[arg] = value

        return request_dict

    def look_for_order(self):
        pass

