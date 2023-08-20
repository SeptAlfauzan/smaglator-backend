from time import sleep
from mqtt import send_message, start_connection


# client = start_connection()
# client.loop_start()

# send_message(client=client, message="send from client 1", topic="encyclopedia/wheater")

# # single_publish(message="test dari local", topic="encyclopedia/wheater")


# # client.loop_forever()
# client.loop_stop()

client = start_connection()
client.loop_start()
send_message(client=client, message="msg", topic="encyclopedia/wheater")
client.loop_stop()
