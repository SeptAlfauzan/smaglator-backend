import time
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

from paho import mqtt

hostname = "a13dfc6212324ee09a5de48f1f2d94dd.s1.eu.hivemq.cloud"


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("connect received with code %s." % rc)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def _init() -> paho.Client:
    try:
        # using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
        # userdata is user defined data of any type, updated by user_data_set()
        # client_id is the given name of the client
        client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
        client.on_connect = on_connect

        # enable TLS for secure connection
        client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        # set username and password
        client.username_pw_set("smaglator", "smaglatorkey")
        return client
    except Exception as e:
        raise e("unable connect create mqtt client")


def start_connection() -> paho.Client:
    try:
        client = _init()
        # connect to HiveMQ Cloud on port 8883 (default for MQTT)
        client.connect(hostname, 8883)

        # setting callbacks, use separate functions like above for better visibility
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.on_publish = on_publish
        return client
    except Exception as e:
        raise e


def send_message(client: paho.Client, message: str, topic: str, qos: int = 1):
    client.publish(topic=topic, payload=message, qos=qos)


def disconnect_after_publish(client: paho.Client):
    client.loop_stop()
    client.disconnect()


def listned_message(client: paho.Client, topic: str, qos: int = 1):
    client.on_message
