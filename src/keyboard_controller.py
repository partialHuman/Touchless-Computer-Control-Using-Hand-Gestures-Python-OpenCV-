import time
import cv2
import pyautogui

from src.hand_tracker import HandTracker


class KeyboardController:
    def __init__(
        self,
        camera_width=640,
        camera_height=480,
        detection_confidence=0.8,
        cooldown=1.0,
    ):
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.cooldown = cooldown
        self.last_action_time = 0

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

        self.hand_tracker = HandTracker(
            max_hands=1,
            detection_confidence=detection_confidence,
        )

    def can_perform_action(self):
        """Prevent the same action from triggering repeatedly."""
        current_time = time.time()

        if current_time - self.last_action_time >= self.cooldown:
            self.last_action_time = current_time
            return True

        return False

    def perform_action(self, fingers, hand_type):
        """
        Perform keyboard actions based on detected fingers.

        fingers format:
        [Thumb, Index, Middle, Ring, Pinky]

        1 = finger up
        0 = finger down
        """

        if not self.can_perform_action():
            return

        # -----------------------------------------
        # LEFT HAND CONTROLS
        # -----------------------------------------
        if hand_type == "Left":

            # Index + Middle -> Previous / Left arrow
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("left")
                print("LEFT ARROW")

            # Thumb only -> Space
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("space")
                print("SPACE")

            # Index only -> Alt + Tab
            elif fingers == [0, 1, 0, 0, 0]:
                pyautogui.hotkey("alt", "tab")
                print("ALT + TAB")

        # -----------------------------------------
        # RIGHT HAND CONTROLS
        # -----------------------------------------
        elif hand_type == "Right":

            # Index + Middle -> Next / Right arrow
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("right")
                print("RIGHT ARROW")

            # Thumb only -> Escape
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("esc")
                print("ESC")

            # Index only -> Refresh
            elif fingers == [0, 1, 0, 0, 0]:
                pyautogui.press("f5")
                print("F5")

    def run(self):
        """Start the virtual keyboard controller."""

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        print("Keyboard Controller started.")
        print("Press 'q' or close the camera window to exit.")

        try:
            while True:
                success, frame = self.cap.read()

                if not success:
                    print("Error: Could not read camera frame.")
                    break

                frame = cv2.flip(frame, 1)

                hands = self.hand_tracker.find_hands(frame)

                for hand in hands:
                    fingers = self.hand_tracker.fingers_up(hand)

                    # Hand type after the fixes we made
                    hand_type = hand["type"]

                    self.perform_action(fingers, hand_type)

                    cv2.putText(
                        frame,
                        f"{hand_type}: {fingers}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )

                cv2.imshow("Touchless Keyboard Controller", frame)

                # Press q to exit
                key = cv2.waitKey(1) & 0xFF

                if key == ord("q"):
                    break

                # Exit when the window is closed
                if cv2.getWindowProperty(
                    "Touchless Keyboard Controller",
                    cv2.WND_PROP_VISIBLE,
                ) < 1:
                    break

        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            self.hand_tracker.close()

            print("Keyboard Controller stopped.")