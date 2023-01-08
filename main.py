from application.utils.EventManager import EventManager
from rules import rules

COMMUNICATION_FOLDER = '../../communication/requests'
FILE_PATTERN = 'request_*'

event_manager = EventManager(COMMUNICATION_FOLDER)
event_manager.start(FILE_PATTERN)
