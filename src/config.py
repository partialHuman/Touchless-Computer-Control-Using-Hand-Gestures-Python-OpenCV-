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
# GESTURE CONFIGURATION
# ---------------------------------------------------------

GESTURES = {
    "move": [0, 1, 0, 0, 0],
    "drag": [0, 1, 1, 0, 0],
}

# ---------------------------------------------------------
# GESTURE ACTIONS
# ---------------------------------------------------------

GESTURE_ACTIONS = {
    "move": "move_cursor",
    "drag": "drag_mouse",
    "unknown": "none",
    "no_hand": "none",
}

# ---------------------------------------------------------
# MOUSE MOVEMENT
# ---------------------------------------------------------

MOUSE_SMOOTHING = 0.25

# ---------------------------------------------------------
# MOUSE ACTIVE REGION
# ---------------------------------------------------------

MOUSE_ACTIVE_REGION_MARGIN = 100

# ---------------------------------------------------------
# MOUSE DRAG
# ---------------------------------------------------------

DRAG_ENABLED = True

# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

HAND_LANDMARKER_MODEL = "models/hand_landmarker.task"