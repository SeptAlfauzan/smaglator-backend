from time import sleep
import time
import paho.mqtt.client as paho
from mqtt import MQTTService


# client = start_connection()
# client.loop_start()

# send_message(client=client, message="send from client 1", topic="encyclopedia/wheater")

# # single_publish(message="test dari local", topic="encyclopedia/wheater")


# # client.loop_forever()
# client.loop_stop()
# send_message(client=client, message="msg", topic="encyclopedia/wheater")
# client.loop_stop()
def on_message(client: paho.Client, userdata: any, msg: paho.MQTTMessage):
    payload = msg.payload
    decoded_payload = payload.decode("ascii")

    if decoded_payload == "connect":
        print("start connection..")
    elif decoded_payload == "disconnect":
        print("stop connection..")
    else:
        print("command invalid")
        print(msg.payload)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.publish("topic/test", "Hello MQTT")


mqtt = MQTTService()
client = mqtt.start_connection()
client.loop_start()
client.subscribe("smaglator/client", qos=0)
client.publish("smaglator/client", "connect")
client.on_message = on_message
time.sleep(2)
client.loop_stop()
