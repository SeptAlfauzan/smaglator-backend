from fastapi import APIRouter, HTTPException

from app.controller.mqtt_controller import MQTTController


MQTTRouter = APIRouter(prefix="/api/v1/mqtt", tags=["mqtt"])


@MQTTRouter.post("/signal")
def index(input: bool, topic: str):
    try:
        message: str = "1" if input == True else "0"

        message_response = "Signal {msg} success send to {topic}".format(
            msg=message, topic=topic
        )
        controller = MQTTController()
        controller.send_message(msg="message", topic=topic)

        return {
            "data": {"signal_send": message, "topic": topic},
            "message": message_response,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: " + str(e))
