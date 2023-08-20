import unittest


class TestObjectDetection(unittest.TestCase):
    from app.services.object_detection_service import predict_handgesture_language

    def test_result_detection(self):
        prediction = self.predict_handgesture_language(
            "./../app/assets/model/datasetsibi.h5"
        )
        # prediction = -2
        self.assertEqual(prediction, -2)


if __name__ == "__main__":
    unittest.main()
