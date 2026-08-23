import math

from src.config import (
    CLICK_DISTANCE_THRESHOLD,
    GESTURES,
    GESTURE_ACTIONS,
)


class GestureDetector:
    def __init__(
        self,
        click_threshold=CLICK_DISTANCE_THRESHOLD,
    ):
        self.click_threshold = click_threshold
        self.current_gesture = None
        self.previous_gesture = None

    def get_fingers_up(
        self,
        landmarks,
        hand_type,
    ):
        """
        Determine which fingers are raised.

        Returns:
            [thumb, index, middle, ring, pinky]

        1 = finger is up
        0 = finger is down
        """

        fingers = []

        # =============================================
        # THUMB
        # =============================================

        # For a mirrored camera frame, the horizontal
        # relationship differs for left and right hands.

        thumb_tip_x = landmarks[4].x
        thumb_ip_x = landmarks[3].x

        if hand_type == "Right":
            thumb_up = (
                thumb_tip_x < thumb_ip_x
            )
        else:
            thumb_up = (
                thumb_tip_x > thumb_ip_x
            )

        fingers.append(
            1 if thumb_up else 0
        )

        # =============================================
        # INDEX, MIDDLE, RING, PINKY
        # =============================================

        finger_tip_ids = [8, 12, 16, 20]
        finger_pip_ids = [6, 10, 14, 18]

        for tip_id, pip_id in zip(
            finger_tip_ids,
            finger_pip_ids,
        ):
            finger_up = (
                landmarks[tip_id].y
                < landmarks[pip_id].y
            )

            fingers.append(
                1 if finger_up else 0
            )

        return fingers

    def get_finger_gesture(self, fingers):
        """
        Identify a gesture based on
        the configured finger pattern.

        Returns:
            str: Gesture name.
        """

        if fingers == GESTURES["drag"]:
            return "drag"

        if fingers == GESTURES["move"]:
            return "move"

        return "unknown"

    def update_gesture_state(self, gesture):
        """
        Update gesture state.

        Returns:
            True if this is a newly detected gesture.
            False if the same gesture is continuing.
        """

        self.previous_gesture = self.current_gesture
        self.current_gesture = gesture

        return (
            self.current_gesture
            != self.previous_gesture
        )

    def get_gesture_action(self, gesture):
        """
        Return the configured action
        for a detected gesture.
        """

        return GESTURE_ACTIONS.get(
            gesture,
            "none",
        )

    def is_click_gesture(
        self,
        index_x,
        index_y,
        thumb_x,
        thumb_y,
    ):
        """
        Detect a thumb + index pinch.

        Returns:
            tuple:
                (is_click, distance)
        """

        distance = math.hypot(
            index_x - thumb_x,
            index_y - thumb_y,
        )

        is_click = (
            distance < self.click_threshold
        )

        return is_click, distance