from app.adder import kafka_sender
from app.adder import request_converter
from app.utils import json_converter

from flask import Request


def add_event_to_kafka(request: Request, config: dict, event_type: str):
    event = request_converter.convert_request_to_model(request)
    json_event = json_converter.convert_to_json(event)
    kafka_sender.send(json_event, config, event_type)
