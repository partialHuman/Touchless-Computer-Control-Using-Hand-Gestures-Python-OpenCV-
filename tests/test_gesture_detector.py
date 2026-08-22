from src.gesture_detector import GestureDetector


class Landmark:
    """Simple mock MediaPipe landmark."""

    def __init__(self, x=0.5, y=0.5):
        self.x = x
        self.y = y


def create_landmarks():
    """Create 21 default landmarks."""

    return [
        Landmark()
        for _ in range(21)
    ]


# =========================================================
# HANDEDNESS TESTS
# =========================================================

def test_correct_left_handedness():
    detector = GestureDetector()

    assert (
        detector.get_corrected_handedness("Left")
        == "Right"
    )


def test_correct_right_handedness():
    detector = GestureDetector()

    assert (
        detector.get_corrected_handedness("Right")
        == "Left"
    )


def test_unknown_handedness():
    detector = GestureDetector()

    assert (
        detector.get_corrected_handedness("Unknown")
        == "Unknown"
    )


# =========================================================
# THUMB TESTS
# =========================================================

def test_right_hand_thumb_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Right hand:
    # Thumb tip left of thumb joint
    landmarks[4] = Landmark(x=0.3)
    landmarks[3] = Landmark(x=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers[0] == 1


def test_right_hand_thumb_down():
    detector = GestureDetector()
    landmarks = create_landmarks()

    landmarks[4] = Landmark(x=0.7)
    landmarks[3] = Landmark(x=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers[0] == 0


def test_left_hand_thumb_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Left hand:
    # Thumb tip right of thumb joint
    landmarks[4] = Landmark(x=0.7)
    landmarks[3] = Landmark(x=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Left",
    )

    assert fingers[0] == 1


def test_left_hand_thumb_down():
    detector = GestureDetector()
    landmarks = create_landmarks()

    landmarks[4] = Landmark(x=0.3)
    landmarks[3] = Landmark(x=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Left",
    )

    assert fingers[0] == 0


# =========================================================
# FINGER TESTS
# =========================================================

def test_index_finger_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Tip is above PIP joint
    landmarks[8] = Landmark(y=0.3)
    landmarks[6] = Landmark(y=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers[1] == 1


def test_index_finger_down():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Tip is below PIP joint
    landmarks[8] = Landmark(y=0.7)
    landmarks[6] = Landmark(y=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers[1] == 0


def test_index_and_middle_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Index
    landmarks[8] = Landmark(y=0.3)
    landmarks[6] = Landmark(y=0.5)

    # Middle
    landmarks[12] = Landmark(y=0.3)
    landmarks[10] = Landmark(y=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers == [0, 1, 1, 0, 0]


def test_all_fingers_up():
    detector = GestureDetector()
    landmarks = create_landmarks()

    # Right-hand thumb
    landmarks[4] = Landmark(x=0.3)
    landmarks[3] = Landmark(x=0.5)

    # Index
    landmarks[8] = Landmark(y=0.3)
    landmarks[6] = Landmark(y=0.5)

    # Middle
    landmarks[12] = Landmark(y=0.3)
    landmarks[10] = Landmark(y=0.5)

    # Ring
    landmarks[16] = Landmark(y=0.3)
    landmarks[14] = Landmark(y=0.5)

    # Pinky
    landmarks[20] = Landmark(y=0.3)
    landmarks[18] = Landmark(y=0.5)

    fingers = detector.get_fingers_up(
        landmarks,
        "Right",
    )

    assert fingers == [1, 1, 1, 1, 1]