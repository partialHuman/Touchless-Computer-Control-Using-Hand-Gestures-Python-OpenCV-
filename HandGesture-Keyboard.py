import time

import cv2
import mediapipe as mp
import pyautogui


# =========================================================
# CONFIGURATION
# =========================================================

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

MODEL_PATH = "hand_landmarker.task"

GESTURE_COOLDOWN = 1.0


# =========================================================
# MEDIAPIPE SETUP
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


last_action_time = 0


# =========================================================
# FINGER DETECTION
# =========================================================

def get_fingers_up(landmarks, handedness):
    """
    Returns finger state in the format:

    [thumb, index, middle, ring, pinky]

    1 = finger up
    0 = finger down
    """

    fingers = []

    # -----------------------------------------------------
    # THUMB
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # OTHER FOUR FINGERS
    # -----------------------------------------------------

    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip_id, pip_id in zip(finger_tips, finger_pips):

        if landmarks[tip_id].y < landmarks[pip_id].y:
            fingers.append(1)

        else:
            fingers.append(0)

    return fingers


# =========================================================
# MAIN LOOP
# =========================================================

with HandLandmarker.create_from_options(options) as hand_detector:

    while True:

        success, frame = cap.read()

        if not success:
            print("Failed to read from camera.")
            break

        # Mirror camera
        frame = cv2.flip(frame, 1)

        frame_height, frame_width, _ = frame.shape

        # Convert frame
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        timestamp_ms = int(time.time() * 1000)

        result = hand_detector.detect_for_video(
            mp_image,
            timestamp_ms
        )

        # =================================================
        # HAND DETECTED
        # =================================================

        if result.hand_landmarks:

            landmarks = result.hand_landmarks[0]

            # Get detected hand label
            detected_hand = result.handedness[0][0].category_name

            # The camera frame is mirrored, so swap handedness
            if detected_hand == "Left":
                handedness = "Right"
            else:
                handedness = "Left"

            # Finger state
            fingers = get_fingers_up(
                landmarks,
                handedness
            )

            print(
                f"Hand: {handedness} | Fingers: {fingers}"
            )

            # Draw landmarks
            for landmark in landmarks:

                x = int(
                    landmark.x * frame_width
                )

                y = int(
                    landmark.y * frame_height
                )

                cv2.circle(
                    frame,
                    (x, y),
                    4,
                    (0, 255, 0),
                    -1
                )

            # =============================================
            # GESTURE COOLDOWN
            # =============================================

            current_time = time.time()

            if (
                current_time - last_action_time
                > GESTURE_COOLDOWN
            ):

                # =========================================
                # LEFT HAND
                # =========================================

                if handedness == "Left":

                    # Two fingers
                    if fingers == [0, 1, 1, 0, 0]:

                        pyautogui.press("left")

                        print("Left")

                        last_action_time = current_time

                    # Thumb
                    elif fingers == [1, 0, 0, 0, 0]:

                        pyautogui.press("space")

                        print("Space")

                        last_action_time = current_time

                    # Index finger
                    elif fingers == [0, 1, 0, 0, 0]:

                        pyautogui.hotkey(
                            "alt",
                            "tab"
                        )

                        print("Alt + Tab")

                        last_action_time = current_time

                # =========================================
                # RIGHT HAND
                # =========================================

                elif handedness == "Right":

                    # Two fingers
                    if fingers == [0, 1, 1, 0, 0]:

                        pyautogui.press("right")

                        print("Right")

                        last_action_time = current_time

                    # Thumb
                    elif fingers == [1, 0, 0, 0, 0]:

                        pyautogui.press("esc")

                        print("Esc")

                        last_action_time = current_time

                    # Index finger
                    elif fingers == [0, 1, 0, 0, 0]:

                        pyautogui.press("f5")

                        print("F5")

                        last_action_time = current_time

        # =================================================
        # DISPLAY
        # =================================================

        window_name = "Hand Gesture Keyboard"

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