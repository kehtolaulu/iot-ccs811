import json

from paho.mqtt.client import Client
from subscriber import Subscriber


class MqttSender(Subscriber):
    def __init__(self, client: Client, topic: str):
        self.client = client
        self.topic = topic


    def on_next(self, message: dict):
        self.client.publish(self.topic, json.dumps(message))
