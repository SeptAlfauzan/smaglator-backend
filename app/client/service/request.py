from model.hand_features_model import HandGestureFeaturesModel


def convert_np_to_model(values):
    attribute_names = (
        [f"x{i}" for i in range(1, 22)]
        + [f"y{i}" for i in range(1, 22)]
        + [f"z{i}" for i in range(1, 22)]
        + [f"v{i}" for i in range(1, 22)]
    )
    data_dict = {name: value for name, value in zip(attribute_names, values)}
    hand_gesture = HandGestureFeaturesModel(**data_dict)
    print(hand_gesture)
    return hand_gesture
