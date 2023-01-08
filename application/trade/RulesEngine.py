import re
from typing import Set

from application.trade.ArgTypes import ResponseType
from application.trade.Order import Order


class RulesEngine:
    """
    A class to evaluate and apply the rules defined
    """
    RULES = set()

    def __init__(self, rules_module):
        self.rules_module = rules_module
        self.collect_rules()

    def collect_rules(self):
        """
        Collect the rules from the rules module
        :return:
        """
        for attr in dir(self.rules_module):
            if re.match('rule_*', attr):
                self.RULES.add(getattr(self.rules_module, attr))

    def process_order(self, order: Order) -> Set[ResponseType]:
        """
        Apply the rules to the given order
        :param order: The incoming order
        :return: list of ResponseTypes
        """
        response_types = set()

        for rule in self.RULES:
            response_types.add(rule(order))

        if ResponseType.REJECT in response_types:
            response_types = {ResponseType.REJECT}

        return response_types


if __name__ == '__main__':
    from rules import rules
    engine = RulesEngine(rules)
    print(engine.collect_rules())
