import cv2
import mediapipe as mp

from src.config import (
    HAND_DETECTION_CONFIDENCE,
    HAND_LANDMARKER_MODEL,
    HAND_PRESENCE_CONFIDENCE,
    HAND_TRACKING_CONFIDENCE,
    MAX_HANDS,
)
from src.gesture_detector import GestureDetector


class HandTracker:
    def __init__(
        self,
        model_path=HAND_LANDMARKER_MODEL,
        max_hands=MAX_HANDS,
        detection_confidence=HAND_DETECTION_CONFIDENCE,
        presence_confidence=HAND_PRESENCE_CONFIDENCE,
        tracking_confidence=HAND_TRACKING_CONFIDENCE,
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
        Detect hands in an OpenCV frame.

        Returns a list of dictionaries containing:
        - type: Corrected Left/Right handedness
        - landmarks: MediaPipe normalized landmarks
        - lmList: Pixel coordinates
        """

        frame_height, frame_width, _ = frame.shape

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB,
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame,
        )

        result = self.detector.detect(mp_image)

        hands = []

        if not result.hand_landmarks:
            return hands

        for landmarks, handedness_data in zip(
            result.hand_landmarks,
            result.handedness,
        ):
            detected_hand = (
                handedness_data[0].category_name
            )

            # Correct handedness because the frame is mirrored
            hand_type = self.get_corrected_handedness(
                detected_hand
            )

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

    def get_corrected_handedness(self, handedness):
        """
        Correct left/right hand labeling because the
        camera frame is mirrored.
        """

        if handedness == "Left":
            return "Right"

        if handedness == "Right":
            return "Left"

        return handedness

    def fingers_up(self, hand):
        """
        Return finger states.

        Format:
        [thumb, index, middle, ring, pinky]
        """

        return self.gesture_detector.get_fingers_up(
            hand["landmarks"],
            hand["type"],
        )

    def close(self):
        """Release MediaPipe resources."""

        self.detector.close()