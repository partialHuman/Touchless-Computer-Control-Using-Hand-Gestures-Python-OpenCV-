# Testing Guide

This document describes the testing performed for the Touchless Computer Control project.

---

# Testing Overview

The project includes:

- Automated tests for gesture detection logic.
- Manual testing for Virtual Mouse functionality.
- Manual testing for Gesture Keyboard functionality.
- Application startup and cleanup testing.

The test files are located in:

```text
tests/
└── test_gesture_detector.py
```
---
# Automated Testing

### Running the Tests

Activate the virtual environment:

### Windows
```
.venv\Scripts\Activate.ps1
```
Run the test suite:
```
pytest
```
Or run the tests explicitly:
```
pytest tests/
```
To run with verbose output:
```
pytest -v
```
---
# Gesture Detector Testing

The automated tests verify the gesture detection logic implemented in:
```
src/gesture_detector.py
```
The tests are located in:
```
tests/test_gesture_detector.py
```
The tested functionality includes gesture recognition based on finger-state patterns.

Finger states follow the format:
```
[Thumb, Index, Middle, Ring, Pinky]
```
Examples of supported patterns include:

|Finger State|	Expected Gesture|
|--|--|
|[1, 0, 0, 0, 0]|	Thumb|
|[0, 1, 0, 0, 0]|	Index Finger|
|[0, 1, 1, 0, 0]|	Index + Middle|

Unsupported patterns should not trigger a configured gesture action.

---

# Manual Testing

Because the project interacts with a physical webcam and controls the operating system through PyAutoGUI, several features are tested manually.


# Application Startup Testing

Run:
```
python main.py
```
#### Verify:
- Application starts successfully.
-  Controller selection menu is displayed.
- Virtual Mouse mode can be selected.
- Gesture Keyboard mode can be selected.
- Camera opens successfully.

Expected menu:
1. Virtual Mouse
2. Gesture Keyboard

---

# Virtual Mouse Testing

## Cursor Movement

Test procedure:
1. Start Virtual Mouse mode.
2. Keep the hand visible to the camera.
3. Move the index finger.

Expected result:
- System cursor follows the index fingertip.
- Cursor movement is smoothed.
- Cursor movement remains stable during normal operation.

## Left Click

Test procedure:
1. Move the index finger over a target.
2. Bring the thumb and index fingertips close together.

Expected result:
- A left mouse click is triggered.
- Click cooldown prevents rapid repeated clicks.

## Drag

Test procedure:
1. Raise the index and middle fingers.
2. Move the hand.
3. Change the gesture or remove the hand from the camera.

Expected result:
- Dragging begins when Index + Middle is detected.
- The left mouse button remains held during the gesture.
- Dragging stops when the gesture changes.
- Dragging stops when the hand disappears.

---

# Gesture Keyboard Testing

## Hand Detection

Test procedure:

1. Start Gesture Keyboard mode.
2. Place either hand in front of the camera.

Expected result:

- Hand detection works.
- Left and Right hand identification works correctly.
- Finger states are detected correctly.
- No-hand state does not trigger an action.

## Default Profile

The default keyboard profile was tested using the following mappings.

### Left Hand
|Gesture|	Expected Action|	Status|
|--|--|--|
|Index + Middle|	Left Arrow|	Tested|
|Thumb	|Space|	Tested|
|Index Finger|	Alt + Tab|	Tested|

### Right Hand
|Gesture	|Expected Action|	Status|
|--|--|--|
|Index + Middle|	Right| Arrow	Tested|
|Thumb	|Escape|	Tested|
|Index Finger|	F5|	Tested|

## Presentation Profile

The presentation profile can be tested by changing:
```
KEYBOARD_PROFILE = "presentation"
```
Verify that gestures trigger the actions configured for that profile.

|Hand|	Gesture	|Expected Action|
|--|--|--|
|Left|	Index + Middle|	Left Arrow|
|Left|	Thumb	|Space|
|Left|	Index	|Escape|
|Right|	Index + Middle|	Right Arrow|
|Right|	Thumb	|Space|
|Right|	Index	|F5|

---

# Window Exit Testing

Both controller modes support two exit methods.

### Exit Using `Q`

With the camera window active:
```
Q
```
Expected result:

- Controller loop stops.
- Camera is released.
- OpenCV window closes.
- MediaPipe resources are released.

## Exit Using the Window Close Button

Click the `X` on the camera window.

Expected result:

- Application detects the closed window.
- Controller loop terminates.
- Camera is released.
- OpenCV windows are destroyed.
- MediaPipe resources are released.

---
# Regression Testing Checklist

Before merging future changes, verify:
```
Application
[ ] Application starts successfully
[ ] Menu displays correctly
[ ] Mouse mode starts
[ ] Keyboard mode starts

Hand Detection
[ ] Left hand detected correctly
[ ] Right hand detected correctly
[ ] Finger states detected correctly

Virtual Mouse
[ ] Cursor movement works
[ ] Click gesture works
[ ] Drag gesture works
[ ] Drag stops safely

Gesture Keyboard
[ ] Default profile works
[ ] Presentation profile works
[ ] Gesture labels display correctly
[ ] Action labels display correctly
[ ] Cooldown prevents repeated actions

Exit Handling
[ ] Q exits correctly
[ ] Window X exits correctly
[ ] Camera is released
```
# Future Testing Improvements

Potential testing improvements include:
- Unit tests for keyboard action mapping.
- Unit tests for keyboard profiles.
- Unit tests for mouse gesture detection.
- Mocked PyAutoGUI tests.
- Camera input simulation.
- Automated integration tests.
- Continuous integration using GitHub Actions.
- Code coverage reporting.