#!/usr/bin/env python3

import busio
import adafruit_ccs811

from board import SCL, SDA
from os import environ as env
from paho.mqtt.client import Client


def get_eco2() -> Css811Eco2:
    i2c = busio.I2C(SCL, SDA)
    ccs811 = adafruit_ccs811.CCS811(i2c)
    return Css811Eco2(ccs811, 0.5)


def get_mqtt_sender() -> MqttSender:
    def raise_on_error(_client, _userdata, _flags, result_code):
        raise Exception("Error connecting to MQTT!")

    client_id = env.get('BROKER_CLIENT_ID')
    host, port = env.get('BROKER_HOST'), env.get('BROKER_PORT')
    username, password = env.get('BROKER_CLIENT_USERNAME'), env.get('BROKER_CLIENT_PASSWORD')
    topic = env.get('BROKER_TOPIC')

    client = Client(client_id)
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

    if username and password:
        client.username_pw_set(username, password)

    client.on_connect = raise_on_error
    client.connect(host, port)
    return MqttSender(client,)

if __name__ == '__main__':
    eco2 = get_eco2()
    mqtt_sender = get_mqtt_sender()
    eco2.subscribe(mqtt_sender)
    eco2.run()
