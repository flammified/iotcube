import time
from gattlib import GATTRequester
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    pass


def on_message(client, userdata, msg):
    pass
    # print(msg)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", port=1883)


class PYRRequester(GATTRequester):
    def on_notification(self, handle, data):
        print(data[3:])
        # for c in data:
        #     print(c)
        client.publish("orientation", payload=str(data[3:]))


req = PYRRequester("A8:1B:6A:A9:DB:8D")

while True:
    # here, do other interesting things
    time.sleep(100)
    client.loop()
