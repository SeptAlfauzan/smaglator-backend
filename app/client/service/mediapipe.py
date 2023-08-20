import mediapipe as mp
import cv2


class MediaPipeService:
    is_running = False
    cap = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    def start(self):
        self.is_running = True

        while self.is_running:
            with mp.solutions.hands.Hands(
                min_detection_confidence=0.5, min_tracking_confidence=0.5
            ) as hands:
                while self.cap.isOpened():
                    ret, frame = self.cap.read()

                    if not ret:
                        print("Gagal membaca frame")
                        break

                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False

                    results = hands.process(image)

                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            mp.solutions.drawing_utils.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp.solutions.hands.HAND_CONNECTIONS,
                                mp.solutions.drawing_utils.DrawingSpec(
                                    color=(80, 22, 10), thickness=2, circle_radius=4
                                ),
                                mp.solutions.drawing_utils.DrawingSpec(
                                    color=(80, 44, 121), thickness=2, circle_radius=2
                                ),
                            )

                    cv2.imshow("Raw Webcam Feed", image)

                    if cv2.waitKey(10) & 0xFF == ord("q"):
                        break

    def close(self):
        self.is_running = False
        self.cap.release()
        cv2.destroyAllWindows()

    def on_message(self, client, userdata, message):
        # Handle the MQTT message here
        if message.topic == "close_opencv":
            self.close()
