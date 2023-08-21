from services.mqtt import MQTTService
from service.mediapipe import MediaPipeService
import paho.mqtt.client as mqtt
import threading
from dotenv import load_dotenv
import os

load_dotenv()


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("smaglator/client")


mediapipe_service = MediaPipeService()
mqtt_service = MQTTService()
mqtt_client = mqtt_service.start_connection()
mqtt_client.loop_start()

mqtt_client.connect(os.getenv("MQTT_URL"), int(os.getenv("MQTT_PORT")), 60)
mqtt_thread = threading.Thread(target=mqtt_client.loop_start)
mqtt_thread.start()

mqtt_client.on_connect = on_connect

# Start the MediaPipeService in a separate thread
mediapipe_thread = threading.Thread(target=mediapipe_service.start)
mediapipe_thread.start()

# Wait for a key press to close the window
input("Press Enter to close...")
# Stop the MQTT client and wait for the threads to finish
mqtt_client.loop_stop()
mqtt_thread.join()
mediapipe_service.close()
mediapipe_thread.join()

print("Window closed")
