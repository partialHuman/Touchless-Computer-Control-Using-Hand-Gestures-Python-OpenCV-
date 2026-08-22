from src.gesture_detector import GestureDetector


class Landmark:
    """Simple mock landmark for testing."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_landmarks():
    """Create 21 default landmarks."""

    return [
        Landmark(0.5, 0.5)
        for _ in range(21)
    ]


def test_corrected_handedness():
    detector = GestureDetector()

    assert detector.get_corrected_handedness("Left") == "Right"
    assert detector.get_corrected_handedness("Right") == "Left"


def test_right_hand_thumb_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Right hand:
    # thumb tip must be left of thumb IP
    landmarks[4] = Landmark(0.3, 0.5)
    landmarks[3] = Landmark(0.5, 0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers[0] == 1


def test_left_hand_thumb_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Left hand:
    # thumb tip must be right of thumb IP
    landmarks[4] = Landmark(0.7, 0.5)
    landmarks[3] = Landmark(0.5, 0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Left",
    )

    assert fingers[0] == 1