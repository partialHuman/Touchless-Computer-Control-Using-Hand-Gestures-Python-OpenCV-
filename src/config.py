"""
Application configuration constants.
"""

# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

HAND_LANDMARKER_MODEL = "models/hand_landmarker.task"

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
# KEYBOARD GESTURES
# ---------------------------------------------------------

KEYBOARD_GESTURES = {
    "left_right": [0, 1, 1, 0, 0],
    "thumb": [1, 0, 0, 0, 0],
    "index": [0, 1, 0, 0, 0],
}

# ---------------------------------------------------------
# KEYBOARD DISPLAY LABELS
# ---------------------------------------------------------

KEYBOARD_GESTURE_LABELS = {
    "left_right": "Index + Middle",
    "thumb": "Thumb",
    "index": "Index Finger",
    "unknown": "Unknown",
}


KEYBOARD_ACTION_LABELS = {
    "left": "Left Arrow",
    "right": "Right Arrow",
    "space": "Space",
    "esc": "Escape",
    "f5": "Refresh (F5)",
    "alt+tab": "Alt + Tab",
}

# ---------------------------------------------------------
# KEYBOARD CONTROL PROFILE
# ---------------------------------------------------------

KEYBOARD_PROFILE = "presentation"


KEYBOARD_PROFILES = {

    "default": {
        "Left": {
            "left_right": "left",
            "thumb": "space",
            "index": "alt+tab",
        },

        "Right": {
            "left_right": "right",
            "thumb": "esc",
            "index": "f5",
        },
    },

    "presentation": {
        "Left": {
            "left_right": "left",
            "thumb": "space",
            "index": "esc",
        },

        "Right": {
            "left_right": "right",
            "thumb": "space",
            "index": "f5",
        },
    },

}

