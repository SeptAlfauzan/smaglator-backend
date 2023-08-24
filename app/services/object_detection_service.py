import pickle
from typing import List
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from app.model.hand_gesture_feature import HandGestureFeaturesModel


def predict_handgesture_language(input: List[HandGestureFeaturesModel]) -> List[str]:
    model: RandomForestClassifier = pickle.load(
        open("./app/assets/ml_model/datasetsibi.pkl", "rb")
    )

    data_dict = [data.dict() for data in input]
    input_x = pd.DataFrame.from_dict(data_dict)
    prediction = model.predict(input_x)

    data = np.array(prediction)
    data = data.tolist()

    return data
