import time

import cv2
import pyautogui

from src.config import (
    KEYBOARD_ACTION_COOLDOWN,
    KEYBOARD_CAMERA_HEIGHT,
    KEYBOARD_CAMERA_WIDTH,
)
from src.hand_tracker import HandTracker


class KeyboardController:
    def __init__(self):
        self.camera_width = KEYBOARD_CAMERA_WIDTH
        self.camera_height = KEYBOARD_CAMERA_HEIGHT
        self.action_cooldown = KEYBOARD_ACTION_COOLDOWN

        self.hand_tracker = HandTracker()

        self.last_action_time = 0

    def perform_action(self, hand_type, fingers):
        """Perform an action based on hand type and gesture."""

        current_time = time.time()

        if (
            current_time - self.last_action_time
            < self.action_cooldown
        ):
            return

        action_performed = False

        # LEFT HAND
        if hand_type == "Left":

            # Index + Middle → Left Arrow
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("left")
                print("Left Arrow")
                action_performed = True

            # Thumb → Space
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("space")
                print("Space")
                action_performed = True

            # Index → Alt + Tab
            elif fingers == [0, 1, 0, 0, 0]:
                pyautogui.hotkey("alt", "tab")
                print("Alt + Tab")
                action_performed = True

        # RIGHT HAND
        elif hand_type == "Right":

            # Index + Middle → Right Arrow
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("right")
                print("Right Arrow")
                action_performed = True

            # Thumb → Escape
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("esc")
                print("Escape")
                action_performed = True

            # Index → F5
            elif fingers == [0, 1, 0, 0, 0]:
                pyautogui.press("f5")
                print("F5")
                action_performed = True

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
                print("Error: Unable to read from camera.")
                break

            # Mirror for natural interaction
            frame = cv2.flip(frame, 1)

            hands = self.hand_tracker.find_hands(frame)

            if hands:
                hand = hands[0]

                hand_type = hand["type"]

                fingers = self.hand_tracker.fingers_up(
                    hand
                )

                self.perform_action(
                    hand_type,
                    fingers,
                )

                # Display detected hand and gesture
                cv2.putText(
                    frame,
                    f"{hand_type}: {fingers}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
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