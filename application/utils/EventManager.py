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
            print(f"The communications folder {self.comm_path} does not exist\n")
            raise RuntimeError

    def start(self, file_pattern):
        while True:
            self.load_requests(file_pattern)
            time.sleep(10)

    def load_requests(self, file_pattern):
        files = (self.comm_path / 'requests').glob(file_pattern)
        for file in files:
            if file not in self.CURRENT_FILES:
                request = self.read_request(file)
                responses = self.process_request(request)
                self.send_responses(responses)
                self.CURRENT_FILES.add(file)

    @staticmethod
    def read_request(file):
        with open(file) as request_file:
            request_string = request_file.readlines()[0]
            print(f"Received request: {request_string}\n")
            request = Request.parse(request_string)
            print(f"Read request: {request}\n")
        return request

    def process_request(self, request: Request) -> List[Response]:
        order = Order(request)
        response_types = self.rules_engine.process_order(order)
        responses = Response.generate_response(order, response_types)
        return responses

    def send_responses(self, responses):
        response_path = self.comm_path / 'responses'
        if not response_path.exists():
            response_path.mkdir()

        for a_response in responses:
            order_id = a_response.order_id
            print(f"Generated Response: {a_response}\n")
            response_string = a_response.build_response()
            with open(f"{response_path}/response_{order_id}", 'w') as file:
                file.write(response_string)
            print(f"Sent response for order_id: {order_id}: {response_string}\n")
