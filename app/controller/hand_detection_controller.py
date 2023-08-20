from typing import List
from app.model.hand_gesture_feature import HandGestureFeaturesModel
from app.services.object_detection_service import predict_handgesture_language


class HandDetectionController:
    def create_prediction(input: List[HandGestureFeaturesModel]) -> List[str]:
        prediction = predict_handgesture_language(input=input)
        return prediction
