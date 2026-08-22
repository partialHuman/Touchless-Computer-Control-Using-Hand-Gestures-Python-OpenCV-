from typing import List


class GestureDetector:
    """
    Utility class for hand orientation and finger-state detection.
    """

    FINGER_TIP_IDS = [4, 8, 12, 16, 20]
    FINGER_PIP_IDS = [3, 6, 10, 14, 18]

    def get_corrected_handedness(
        self,
        detected_hand: str,
    ) -> str:
        """
        Correct MediaPipe handedness for a horizontally
        mirrored camera frame.
        """

        if detected_hand == "Left":
            return "Right"

        if detected_hand == "Right":
            return "Left"

        return detected_hand

    def get_fingers_up(
        self,
        landmarks,
        hand_type: str,
    ) -> List[int]:
        """
        Detect which fingers are raised.

        Returns:
            [thumb, index, middle, ring, pinky]

        Each value is:
            1 -> finger is up
            0 -> finger is down
        """

        fingers = []

        # -------------------------------------------------
        # THUMB
        # -------------------------------------------------

        thumb_tip_x = landmarks[4].x
        thumb_joint_x = landmarks[3].x

        if hand_type == "Right":
            thumb_up = int(
                thumb_tip_x < thumb_joint_x
            )

        else:
            thumb_up = int(
                thumb_tip_x > thumb_joint_x
            )

        fingers.append(thumb_up)

        # -------------------------------------------------
        # INDEX, MIDDLE, RING, PINKY
        # -------------------------------------------------

        finger_pairs = [
            (8, 6),    # Index
            (12, 10),  # Middle
            (16, 14),  # Ring
            (20, 18),  # Pinky
        ]

        for tip_id, pip_id in finger_pairs:

            finger_up = int(
                landmarks[tip_id].y
                < landmarks[pip_id].y
            )

            fingers.append(finger_up)

        return fingers