import math
import time

import cv2
import pyautogui

from src.config import (
    DRAG_ENABLED,
    MOUSE_ACTIVE_REGION_MARGIN,
    MOUSE_CAMERA_HEIGHT,
    MOUSE_CAMERA_WIDTH,
    MOUSE_CLICK_COOLDOWN,
    MOUSE_SMOOTHING,
)
from src.hand_tracker import HandTracker
from src.gesture_detector import GestureDetector


class MouseController:
    def __init__(self):
        self.camera_width = MOUSE_CAMERA_WIDTH
        self.camera_height = MOUSE_CAMERA_HEIGHT

        self.click_cooldown = MOUSE_CLICK_COOLDOWN
        self.smoothing = MOUSE_SMOOTHING

        self.hand_tracker = HandTracker()
        self.gesture_detector = GestureDetector()

        self.screen_width, self.screen_height = pyautogui.size()

        # Previous cursor position for smoothing
        self.previous_x = None
        self.previous_y = None

        self.last_click_time = 0

        self.dragging = False

    def get_smoothed_position(self, target_x, target_y):
        """Smoothly interpolate cursor position."""

        # First position: move directly to the target
        if self.previous_x is None:
            self.previous_x = target_x
            self.previous_y = target_y

        # Linear interpolation
        smooth_x = (
            self.previous_x
            + (target_x - self.previous_x) * self.smoothing
        )

        smooth_y = (
            self.previous_y
            + (target_y - self.previous_y) * self.smoothing
        )

        self.previous_x = smooth_x
        self.previous_y = smooth_y

        return smooth_x, smooth_y

    def start_drag(self):
        """Start holding the left mouse button."""

        if not self.dragging:
            pyautogui.mouseDown()
            self.dragging = True
            print("Drag started")


    def stop_drag(self):
        """Release the left mouse button."""

        if self.dragging:
            pyautogui.mouseUp()
            self.dragging = False
            print("Drag stopped")


    def run(self):
        """Run the virtual mouse controller."""

        cap = cv2.VideoCapture(0)

        cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            self.camera_width,
        )

        cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            self.camera_height,
        )

        window_name = "Virtual Mouse"

        while True:
            success, frame = cap.read()

            if not success:
                print("Error: Unable to read from camera.")
                break

            # Mirror camera for natural interaction
            frame = cv2.flip(frame, 1)

            frame_height, frame_width, _ = frame.shape

            margin = MOUSE_ACTIVE_REGION_MARGIN

            active_left = margin
            active_right = frame_width - margin

            active_top = margin
            active_bottom = frame_height - margin

            hands = self.hand_tracker.find_hands(frame)

            gesture_status = "HAND"

            if hands:
                hand = hands[0]
                landmarks = hand["lmList"]

                # Detect raised fingers
                fingers = self.hand_tracker.fingers_up(hand)

                # Identify gesture
                gesture = self.gesture_detector.get_finger_gesture(fingers)

                is_new_gesture = (
                    self.gesture_detector.update_gesture_state(
                        gesture
                    )
                )

                action = self.gesture_detector.get_gesture_action(
                    gesture
                )

                is_move_gesture = (
                    gesture == "move"
                )

                # Index fingertip
                index_x = landmarks[8][0]
                index_y = landmarks[8][1]

                # Thumb fingertip
                thumb_x = landmarks[4][0]
                thumb_y = landmarks[4][1]

                # Draw connection line
                cv2.line(
                    frame,
                    (index_x, index_y),
                    (thumb_x, thumb_y),
                    (255, 255, 0),
                    2,
                )

                # Draw fingertips
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

                cv2.rectangle(
                    frame,
                    (active_left, active_top),
                    (active_right, active_bottom),
                    (255, 0, 255),
                    2,
                )

                # =============================================
                # CURSOR MOVEMENT
                # Only move for MOVE or DRAG actions
                # =============================================

                if action in ("move_cursor", "drag_mouse"):

                    # Keep finger coordinates inside active region
                    clamped_x = max(
                        active_left,
                        min(index_x, active_right),
                    )

                    clamped_y = max(
                        active_top,
                        min(index_y, active_bottom),
                    )

                    # Map active region to full screen
                    target_x = (
                        (clamped_x - active_left)
                        / (active_right - active_left)
                    ) * self.screen_width

                    target_y = (
                        (clamped_y - active_top)
                        / (active_bottom - active_top)
                    ) * self.screen_height
                    
                    # Smooth cursor movement
                    screen_x, screen_y = (
                        self.get_smoothed_position(
                            target_x,
                            target_y,
                        )
                    )

                    pyautogui.moveTo(
                        int(screen_x),
                        int(screen_y),
                    )

                # Current time
                current_time = time.time()

                # =============================================
                # DRAG GESTURE
                # =============================================

                if (
                    DRAG_ENABLED
                    and action == "drag_mouse"
                ):

                    gesture_status = "DRAGGING"

                    self.start_drag()

                    cv2.putText(
                        frame,
                        "DRAGGING",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 0),
                        2,
                    )

                else:
                    # No hand detected
                    self.stop_drag()

                    self.gesture_detector.update_gesture_state(
                        "no_hand"
                    )

                # -------------------------------------------------
                # CLICK GESTURE
                # Thumb + Index pinch
                # -------------------------------------------------

                is_click_gesture, distance = (
                    self.gesture_detector.is_click_gesture(
                        index_x,
                        index_y,
                        thumb_x,
                        thumb_y,
                    )
                )

                if is_click_gesture:

                    gesture_status = "CLICK"

                    if (
                        current_time - self.last_click_time
                        > self.click_cooldown
                    ):
                        pyautogui.click()

                        self.last_click_time = current_time

                        print("Click")

                cv2.putText(
                    frame,
                    f"Distance: {int(distance)}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2,
                )

                # =============================================
                # GESTURE STATUS OVERLAY
                # =============================================

                cv2.rectangle(
                    frame,
                    (10, 10),
                    (260, 60),
                    (30, 30, 30),
                    -1,
                )

                cv2.putText(
                    frame,
                    f"Gesture: {gesture_status}",
                    (20, 45),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

            cv2.imshow(
                window_name,
                frame,
            )

            # Exit with Q
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            # Exit when clicking the window X button
            if (
                cv2.getWindowProperty(
                    window_name,
                    cv2.WND_PROP_VISIBLE,
                )
                < 1
            ):
                break

        self.stop_drag()
        cap.release()
        cv2.destroyAllWindows()
        self.hand_tracker.close()