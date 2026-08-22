import time

import cv2
import mediapipe as mp
import pyautogui


# =========================================================
# CONFIGURATION
# =========================================================

CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

MODEL_PATH = "hand_landmarker.task"

CLICK_THRESHOLD = 20
CLICK_COOLDOWN = 1.0


# =========================================================
# MEDIAPIPE HAND LANDMARKER SETUP
# =========================================================

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1,
)


# =========================================================
# CAMERA SETUP
# =========================================================

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)


screen_width, screen_height = pyautogui.size()

last_click_time = 0


# =========================================================
# MAIN LOOP
# =========================================================

with HandLandmarker.create_from_options(options) as hand_detector:

    while True:

        success, frame = cap.read()

        if not success:
            print("Failed to read from camera.")
            break

        # Mirror the camera for natural mouse control
        frame = cv2.flip(frame, 1)

        frame_height, frame_width, _ = frame.shape

        # Convert OpenCV frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        # Timestamp required for VIDEO mode
        timestamp_ms = int(time.time() * 1000)

        result = hand_detector.detect_for_video(
            mp_image,
            timestamp_ms
        )

        # =================================================
        # HAND DETECTION
        # =================================================

        if result.hand_landmarks:

            landmarks = result.hand_landmarks[0]

            # ---------------------------------------------
            # Draw landmarks
            # ---------------------------------------------

            for landmark in landmarks:

                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                cv2.circle(
                    frame,
                    (x, y),
                    4,
                    (0, 255, 0),
                    -1
                )

            # ---------------------------------------------
            # INDEX FINGER TIP
            # Landmark 8
            # ---------------------------------------------

            index = landmarks[8]

            index_x = int(index.x * frame_width)
            index_y = int(index.y * frame_height)

            cv2.circle(
                frame,
                (index_x, index_y),
                10,
                (0, 255, 255),
                -1
            )

            # Map camera coordinates to screen
            screen_x = screen_width * index_x / frame_width
            screen_y = screen_height * index_y / frame_height

            pyautogui.moveTo(screen_x, screen_y)

            # ---------------------------------------------
            # THUMB TIP
            # Landmark 4
            # ---------------------------------------------

            thumb = landmarks[4]

            thumb_x = int(thumb.x * frame_width)
            thumb_y = int(thumb.y * frame_height)

            cv2.circle(
                frame,
                (thumb_x, thumb_y),
                10,
                (0, 255, 255),
                -1
            )

            # ---------------------------------------------
            # CLICK DETECTION
            # ---------------------------------------------

            distance = abs(index_y - thumb_y)

            current_time = time.time()

            if (
                distance < CLICK_THRESHOLD
                and current_time - last_click_time > CLICK_COOLDOWN
            ):

                pyautogui.click()

                last_click_time = current_time

                print("Click")

        # =================================================
        # DISPLAY
        # =================================================

        window_name = "Virtual Mouse"

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF

        # Exit with Q
        if key == ord("q"):
            break

        # Exit when the window's X button is clicked
        if cv2.getWindowProperty(
            window_name,
            cv2.WND_PROP_VISIBLE
        ) < 1:
            break


# =========================================================
# CLEANUP
# =========================================================

cap.release()
cv2.destroyAllWindows()