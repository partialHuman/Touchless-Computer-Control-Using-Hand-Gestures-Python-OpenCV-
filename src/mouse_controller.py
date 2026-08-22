import cv2
import pyautogui

from src.config import (
    CLICK_DISTANCE_THRESHOLD,
    MOUSE_CAMERA_HEIGHT,
    MOUSE_CAMERA_WIDTH,
    MOUSE_CLICK_COOLDOWN,
)
from src.hand_tracker import HandTracker


class MouseController:
    def __init__(self):
        self.camera_width = MOUSE_CAMERA_WIDTH
        self.camera_height = MOUSE_CAMERA_HEIGHT

        self.click_threshold = CLICK_DISTANCE_THRESHOLD
        self.click_cooldown = MOUSE_CLICK_COOLDOWN

        self.hand_tracker = HandTracker()

        self.screen_width, self.screen_height = pyautogui.size()

    def run(self):
        """Run the virtual mouse controller."""

        cap = cv2.VideoCapture(0)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.camera_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.camera_height)

        last_click_time = 0

        while True:
            success, frame = cap.read()

            if not success:
                print("Error: Unable to read from camera.")
                break

            # Mirror the camera for natural interaction
            frame = cv2.flip(frame, 1)

            frame_height, frame_width, _ = frame.shape

            hands = self.hand_tracker.find_hands(frame)

            if hands:
                hand = hands[0]
                landmarks = hand["lmList"]

                # Index fingertip
                index_x = landmarks[8][0]
                index_y = landmarks[8][1]

                # Thumb fingertip
                thumb_x = landmarks[4][0]
                thumb_y = landmarks[4][1]

                # Draw fingertip indicators
                cv2.circle(
                    frame,
                    (index_x, index_y),
                    10,
                    (0, 255, 255),
                    -1,
                )

                cv2.circle(
                    frame,
                    (thumb_x, thumb_y),
                    10,
                    (0, 255, 255),
                    -1,
                )

                # Map camera coordinates to screen coordinates
                screen_x = (
                    index_x / frame_width
                ) * self.screen_width

                screen_y = (
                    index_y / frame_height
                ) * self.screen_height

                pyautogui.moveTo(screen_x, screen_y)

                # Calculate vertical distance for click gesture
                distance = abs(index_y - thumb_y)

                current_time = cv2.getTickCount() / cv2.getTickFrequency()

                # Click when thumb and index finger are close
                if (
                    distance < self.click_threshold
                    and current_time - last_click_time
                    > self.click_cooldown
                ):
                    pyautogui.click()

                    last_click_time = current_time

                    print("Click")

            cv2.imshow("Virtual Mouse", frame)

            # Exit using Q
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            # Exit if window is closed
            if (
                cv2.getWindowProperty(
                    "Virtual Mouse",
                    cv2.WND_PROP_VISIBLE,
                )
                < 1
            ):
                break

        cap.release()
        cv2.destroyAllWindows()
        self.hand_tracker.close()