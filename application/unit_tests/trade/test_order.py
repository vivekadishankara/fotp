from application.trade.Order import Order


class TestOrder:
    def test_order_attr(self, request_obj):
        order = Order(request_obj)
        assert order.order_id == 480069891
