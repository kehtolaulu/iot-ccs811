import json

from paho.mqtt.client import Client
from subscriber import Subscriber
from datetime import datetime


class MqttSender(Subscriber):
    def __init__(self, client: Client, topic: str):
        self.client = client
        self.topic = topic


    def on_next(self, message: dict):
        json_message = json.dumps(message)
        print(f'[{datetime.now().isoformat()}] Sending: {json_message}')
        self.client.publish(self.topic, json_message)
