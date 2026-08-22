import cv2
import mediapipe as mp

from src.gesture_detector import GestureDetector


class HandTracker:
    def __init__(
        self,
        model_path="models/hand_landmarker.task",
        max_hands=1,
        detection_confidence=0.5,
        presence_confidence=0.5,
        tracking_confidence=0.5,
    ):
        self.gesture_detector = GestureDetector()

        base_options = mp.tasks.BaseOptions(
            model_asset_path=model_path
        )

        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=mp.tasks.vision.RunningMode.IMAGE,
            num_hands=max_hands,
            min_hand_detection_confidence=detection_confidence,
            min_hand_presence_confidence=presence_confidence,
            min_tracking_confidence=tracking_confidence,
        )

        self.detector = (
            mp.tasks.vision.HandLandmarker.create_from_options(
                options
            )
        )

    def find_hands(self, frame):
        """
        Detect hands and return a simplified list.

        Each hand contains:
        - type: Left or Right
        - landmarks: original MediaPipe landmarks
        - lmList: pixel coordinates
        """

        frame_height, frame_width, _ = frame.shape

        # Convert OpenCV BGR frame to RGB
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        # Convert to MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Detect hands
        result = self.detector.detect(mp_image)

        hands = []

        if not result.hand_landmarks:
            return hands

        for landmarks, handedness_data in zip(
            result.hand_landmarks,
            result.handedness,
        ):

            # MediaPipe detected hand
            detected_hand = (
                handedness_data[0].category_name
            )

            # Correct hand because camera frame is mirrored
            hand_type = (
                self.gesture_detector
                .get_corrected_handedness(detected_hand)
            )

            # Convert normalized landmarks to pixels
            lm_list = []

            for landmark in landmarks:
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                lm_list.append([x, y])

            hands.append(
                {
                    "type": hand_type,
                    "landmarks": landmarks,
                    "lmList": lm_list,
                }
            )

        return hands

    def fingers_up(self, hand):
        """
        Return finger states:

        [thumb, index, middle, ring, pinky]
        """

        return self.gesture_detector.get_fingers_up(
            hand["landmarks"],
            hand["type"],
        )

    def close(self):
        """Release MediaPipe resources."""

        self.detector.close()