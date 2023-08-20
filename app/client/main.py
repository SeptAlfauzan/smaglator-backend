from service.mediapipe import MediaPipeService
import paho.mqtt.client as mqtt
import threading


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("client_camera")


mediapipe_service = MediaPipeService()
mqtt_client = mqtt.Client()

mqtt_client.connect("mqtt_broker_address", 1883, 60)
mqtt_thread = threading.Thread(target=mqtt_client.loop_start)
mqtt_thread.start()

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
