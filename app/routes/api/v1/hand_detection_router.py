from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.controller import hand_detection_controller
from app.model.hand_gesture_feature import HandGestureFeaturesModel


HandGestureDetectionRouter = APIRouter(
    prefix="/api/v1/hand-detection", tags=["hand-detection"]
)


@HandGestureDetectionRouter.post("/")
def index(input: List[HandGestureFeaturesModel]):
    try:
        result = hand_detection_controller.predict_handgesture_language(input)
        print(result, isinstance(result, list))
        return {"data": {"predictions": jsonable_encoder(result)}}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: " + str(e))
