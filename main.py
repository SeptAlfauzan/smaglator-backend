from typing import Union

from fastapi import FastAPI
from app.routes.api.v1.hand_detection_router import HandGestureDetectionRouter
from app.routes.api.v1.mqtt_router import MQTTRouter

app = FastAPI(title="SMAGLATOR API")


app.include_router(HandGestureDetectionRouter)
# app.include_router(MQTTRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}
