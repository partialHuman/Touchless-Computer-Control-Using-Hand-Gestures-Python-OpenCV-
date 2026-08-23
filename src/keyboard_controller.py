import time

import cv2

from src.config import (
    KEYBOARD_ACTION_COOLDOWN,
    KEYBOARD_ACTION_LABELS,
    KEYBOARD_CAMERA_HEIGHT,
    KEYBOARD_CAMERA_WIDTH,
    KEYBOARD_GESTURE_LABELS,
    KEYBOARD_GESTURES,
    KEYBOARD_PROFILE,
    KEYBOARD_PROFILES,
)

from src.hand_tracker import HandTracker
from src.keyboard_actions import KeyboardActionExecutor

class KeyboardController:
    def __init__(self):
        self.camera_width = KEYBOARD_CAMERA_WIDTH
        self.camera_height = KEYBOARD_CAMERA_HEIGHT

        self.action_cooldown = (
            KEYBOARD_ACTION_COOLDOWN
        )

        self.hand_tracker = HandTracker()
        self.action_executor = KeyboardActionExecutor()

        self.profile_name = KEYBOARD_PROFILE

        self.profile = KEYBOARD_PROFILES.get(
            self.profile_name,
            KEYBOARD_PROFILES["default"],
        )

        self.last_action_time = 0

        self.current_gesture = None
        self.previous_gesture = None

    def get_gesture_name(self, fingers):
        """
        Convert a finger pattern into
        a configured keyboard gesture.
        """

        for gesture_name, pattern in (
            KEYBOARD_GESTURES.items()
        ):
            if fingers == pattern:
                return gesture_name

        return "unknown"

    def get_action(
        self,
        hand_type,
        gesture,
    ):
        """
        Get the action from the active
        keyboard control profile.
        """

        return self.profile.get(
            hand_type,
            {},
        ).get(
            gesture,
            None,
        )

    def get_gesture_label(self, gesture):
        """Return a user-friendly gesture name."""

        return KEYBOARD_GESTURE_LABELS.get(
            gesture,
            "Unknown",
        )


    def get_action_label(self, action):
        """Return a user-friendly action name."""

        return KEYBOARD_ACTION_LABELS.get(
            action,
            "None",
        )

    def is_new_gesture(self, gesture):
        """
        Return True only when the gesture
        changes from the previous gesture.
        """

        self.previous_gesture = self.current_gesture
        self.current_gesture = gesture

        return (
            self.current_gesture
            != self.previous_gesture
        )

    def perform_action(
        self,
        hand_type,
        fingers,
    ):
        """
        Detect a new gesture and perform
        the configured keyboard action once.
        """

        current_time = time.time()

        gesture = self.get_gesture_name(
            fingers
        )

        # Only trigger when the gesture changes
        if not self.is_new_gesture(gesture):
            return

        # Ignore unknown gestures
        if gesture == "unknown":
            return

        # Cooldown protection
        if (
            current_time
            - self.last_action_time
            < self.action_cooldown
        ):
            return

        action = self.get_action(
            hand_type,
            gesture,
        )

        if action:

            action_performed = (
                self.action_executor.execute(
                    action
                )
            )

            if action_performed:
                self.last_action_time = current_time

    def run(self):
        """Run the gesture keyboard controller."""

        cap = cv2.VideoCapture(0)

        cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            self.camera_width,
        )

        cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            self.camera_height,
        )

        window_name = "Gesture Keyboard"

        while True:
            success, frame = cap.read()

            if not success:
                print(
                    "Error: Unable to read from camera."
                )
                break

            # Mirror for natural interaction
            frame = cv2.flip(
                frame,
                1,
            )

            hands = self.hand_tracker.find_hands(
                frame
            )

            gesture_status = "NO HAND"

            if hands:
                hand = hands[0]

                hand_type = hand["type"]

                fingers = (
                    self.hand_tracker.fingers_up(
                        hand
                    )
                )

                gesture = self.get_gesture_name(
                    fingers
                )

                action = self.get_action(
                    hand_type,
                    gesture,
                )

                gesture_label = self.get_gesture_label(
                    gesture
                )

                action_label = self.get_action_label(
                    action
                )

                gesture_status = (
                    f"{gesture.upper()}"
                )

                self.perform_action(
                    hand_type,
                    fingers,
                )

                # Display hand information
                cv2.putText(
                    frame,
                    f"Hand: {hand_type}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                cv2.putText(
                    frame,
                    f"Gesture: {gesture_label}",
                    (20, 75),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                cv2.putText(
                    frame,
                    f"Action: {action_label}",
                    (20, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

            else:
                # Reset gesture state when hand disappears
                self.current_gesture = None
                self.previous_gesture = None

                cv2.putText(
                    frame,
                    "NO HAND DETECTED",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2,
                )

            cv2.imshow(
                window_name,
                frame,
            )

            # Exit using Q
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            # Exit using window X button
            if (
                cv2.getWindowProperty(
                    window_name,
                    cv2.WND_PROP_VISIBLE,
                )
                < 1
            ):
                break

        cap.release()
        cv2.destroyAllWindows()
        self.hand_tracker.close()