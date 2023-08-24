from service.request import convert_np_to_model
from service.mqtt import MQTTService
from service.mediapipe import MediaPipeService
import paho.mqtt.client as mqtt
import paho.mqtt.client as paho
import threading
from dotenv import load_dotenv
import os

load_dotenv()


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("smaglator/client")


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


mediapipe_service = MediaPipeService()
mqtt_service = MQTTService()

mqtt_client = mqtt_service.start_connection()
mqtt_client.loop_start()
mqtt_client.on_message = on_message


def send_hand_feature_to_broker(hand_feature):
    mqtt_client.publish("smaglator/client", hand_feature)


mqtt_thread = threading.Thread(target=mqtt_client.loop_start)
mqtt_thread.start()

mqtt_client.subscribe("smaglator/client", qos=0)
# Start the MediaPipeService in a separate thread
mediapipe_thread = threading.Thread(
    target=mediapipe_service.start(on_detected=convert_np_to_model)
)
mediapipe_thread.start()

# Wait for a key press to close the window
input("Press Enter to close...")
# Stop the MQTT client and wait for the threads to finish
mqtt_client.loop_stop()
mqtt_thread.join()
mediapipe_service.close()
mediapipe_thread.join()

print("Window closed")
