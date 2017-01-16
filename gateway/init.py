from gattlib import GATTRequester, GATTResponse
import time

class NotifyYourName(GATTResponse):
    def on_response(self, name):
        print("your name is: {}".format(name))


response = NotifyYourName()
req = GATTRequester("A8:1B:6A:A9:DB:8D")
req.read_by_handle_async(0x0003, response)

while True:
    # here, do other interesting things
    time.sleep(1)
