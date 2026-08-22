class GestureDetector:
    @staticmethod
    def get_corrected_handedness(detected_hand):
        """
        Correct MediaPipe handedness because the camera frame
        is mirrored horizontally.
        """
        if detected_hand == "Left":
            return "Right"

        return "Left"

    @staticmethod
    def get_fingers_up(landmarks, handedness):
        """
        Returns finger states in this order:

        [thumb, index, middle, ring, pinky]

        1 = finger extended
        0 = finger folded
        """

        fingers = []

        # -------------------------------
        # Thumb
        # -------------------------------

        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]

        if handedness == "Right":
            fingers.append(
                1 if thumb_tip.x < thumb_ip.x else 0
            )
        else:
            fingers.append(
                1 if thumb_tip.x > thumb_ip.x else 0
            )

        # -------------------------------
        # Index, Middle, Ring, Pinky
        # -------------------------------

        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]

        for tip_id, pip_id in zip(finger_tips, finger_pips):
            if landmarks[tip_id].y < landmarks[pip_id].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers