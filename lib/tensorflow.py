import tensorflow as tf


def load_model(path: str) -> tf.keras.Model:
    model = tf.keras.models.load_model(path)
    return model
