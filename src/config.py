"""
Application configuration constants.
"""

# ---------------------------------------------------------
# CAMERA SETTINGS
# ---------------------------------------------------------

MOUSE_CAMERA_WIDTH = 1280
MOUSE_CAMERA_HEIGHT = 720

KEYBOARD_CAMERA_WIDTH = 640
KEYBOARD_CAMERA_HEIGHT = 480


# ---------------------------------------------------------
# MEDIAPIPE SETTINGS
# ---------------------------------------------------------

MAX_HANDS = 1

HAND_DETECTION_CONFIDENCE = 0.8
HAND_PRESENCE_CONFIDENCE = 0.5
HAND_TRACKING_CONFIDENCE = 0.5


# ---------------------------------------------------------
# GESTURE SETTINGS
# ---------------------------------------------------------

MOUSE_CLICK_COOLDOWN = 0.8
KEYBOARD_ACTION_COOLDOWN = 1.0

CLICK_DISTANCE_THRESHOLD = 20


# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

HAND_LANDMARKER_MODEL = "models/hand_landmarker.task"