from pathlib import Path
import time
from typing import List

from application.comm.Request import Request
from application.comm.Response import Response
from application.trade.Order import Order
from application.trade.RulesEngine import RulesEngine


class EventManager:
    CURRENT_FILES = set()

    def __init__(self, comm_folder_path, rules_module):
        self.comm_path = Path(comm_folder_path)
        self.rules_engine = RulesEngine(rules_module)
        if not self.comm_path.exists():
            raise RuntimeError

    def start(self, file_pattern):
        while True:
            self.load_requests(file_pattern)
            time.sleep(10)

    def load_requests(self, file_pattern):
        files = self.comm_path.glob(file_pattern)
        for file in files:
            if file not in self.CURRENT_FILES:
                request = self.read_request(file)
                responses = self.process_request(request)
                self.CURRENT_FILES.add(file)

    @staticmethod
    def read_request(file):
        with open(file) as request_file:
            request_string = request_file.readlines()[0]
            request = Request.parse(request_string)
        return request

    def process_request(self, request: Request) -> List[Response]:
        order = Order(request)
        response_types = self.rules_engine.process_order(order)
        responses = Response.generate_response(order, response_types)
        return responses
