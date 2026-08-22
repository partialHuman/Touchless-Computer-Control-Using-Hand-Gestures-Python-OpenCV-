import time

import cv2
import pyautogui

from src.hand_tracker import HandTracker


class MouseController:
    def __init__(
        self,
        camera_width=1280,
        camera_height=720,
        detection_confidence=0.8,
        cooldown=0.8,
    ):
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.cooldown = cooldown
        self.last_click_time = 0

        # Camera setup
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

        # Hand tracker
        self.hand_tracker = HandTracker(
            max_hands=1,
            detection_confidence=detection_confidence,
        )

        # Screen size
        self.screen_width, self.screen_height = pyautogui.size()

        # Store index finger position
        self.index_x = 0
        self.index_y = 0

    def can_click(self):
        """Prevent multiple clicks from one gesture."""
        current_time = time.time()

        if current_time - self.last_click_time >= self.cooldown:
            self.last_click_time = current_time
            return True

        return False

    def move_mouse(self, x, y, frame_width, frame_height):
        """Convert camera coordinates to screen coordinates."""

        screen_x = int(
            x * self.screen_width / frame_width
        )

        screen_y = int(
            y * self.screen_height / frame_height
        )

        pyautogui.moveTo(screen_x, screen_y)

    def handle_hand(self, hand, frame):
        """Handle mouse movement and clicking."""

        frame_height, frame_width, _ = frame.shape

        landmarks = hand["lmList"]

        # -----------------------------------------
        # INDEX FINGER → MOVE MOUSE
        # -----------------------------------------
        index_x, index_y = landmarks[8][0], landmarks[8][1]

        self.index_x = index_x
        self.index_y = index_y

        self.move_mouse(
            index_x,
            index_y,
            frame_width,
            frame_height,
        )

        cv2.circle(
            frame,
            (index_x, index_y),
            10,
            (0, 255, 255),
            cv2.FILLED,
        )

        # -----------------------------------------
        # THUMB → CLICK DETECTION
        # -----------------------------------------
        thumb_x, thumb_y = landmarks[4][0], landmarks[4][1]

        cv2.circle(
            frame,
            (thumb_x, thumb_y),
            10,
            (0, 255, 255),
            cv2.FILLED,
        )

        # Distance between thumb and index finger
        distance = abs(self.index_y - thumb_y)

        # Click when thumb and index are close vertically
        if distance < 20 and self.can_click():

            pyautogui.click()

            print("CLICK")

            # Visual feedback
            cv2.putText(
                frame,
                "CLICK",
                (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3,
            )

    def run(self):
        """Start the virtual mouse controller."""

        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            return

        print("Mouse Controller started.")
        print("Press 'q' or close the camera window to exit.")

        try:
            while True:
                success, frame = self.cap.read()

                if not success:
                    print("Error: Could not read camera frame.")
                    break

                # Mirror the camera
                frame = cv2.flip(frame, 1)

                # Detect hands
                hands = self.hand_tracker.find_hands(frame)

                for hand in hands:
                    self.handle_hand(hand, frame)

                # Show camera feed
                cv2.imshow(
                    "Touchless Mouse Controller",
                    frame,
                )

                # Press q to exit
                key = cv2.waitKey(1) & 0xFF

                if key == ord("q"):
                    break

                # Exit when X button is clicked
                if cv2.getWindowProperty(
                    "Touchless Mouse Controller",
                    cv2.WND_PROP_VISIBLE,
                ) < 1:
                    break

        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            self.hand_tracker.close()

            print("Mouse Controller stopped.")