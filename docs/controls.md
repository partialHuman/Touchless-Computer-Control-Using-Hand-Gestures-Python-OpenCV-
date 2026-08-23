# Gesture Controls

This document provides a complete reference for the supported mouse and keyboard gestures.

---

# 1. Virtual Mouse Controls

The Virtual Mouse uses hand landmarks to control the system cursor.

## Cursor Movement

| Gesture | Action |
|---|---|
| Move Index Finger | Move system cursor |

The position of the index fingertip is mapped to the screen coordinates.

Cursor movement is smoothed to reduce jitter.

---

## Left Click

| Gesture | Action |
|---|---|
| Thumb + Index Pinch | Left Mouse Click |

Bring the thumb and index fingertips close together:

```text
Thumb + Index
      ↓
    Pinch
      ↓
 Left Click
```
 A click cooldown helps prevent multiple accidental clicks.

## Drag

| Gesture | Action |
|---|---|
|Index + Middle Fingers Raised|	Hold Left Mouse Button|

While the gesture remains active:
```
Index + Middle
       ↓
     DRAGGING
```
The mouse button is automatically released when:
- The gesture changes.
- The hand disappears.
- The application exits.
---

# 2. Gesture Keyboard Controls

The Gesture Keyboard maps hand gestures to keyboard actions.

The action depends on: `Hand Type + Gesture + Active Profile`

## Default Profile
```
KEYBOARD_PROFILE = "default"
```

### Left Hand

| Gesture | Action |
|---|---|
|Index + Middle |	Left Arrow|
|Thumb	Space|
|Index Finger|	Alt + Tab|

### Right Hand

| Gesture | Action |
|---|---|
|Index + Middle	|Right Arrow|
|Thumb	|Escape|
|Index Finger|	F5 / Refresh|

---

## Presentation Profile
```
KEYBOARD_PROFILE = "presentation"
```

### Left Hand

| Gesture | Action |
|---|---|
|Index + Middle|	Left Arrow|
|Thumb|	Space|
|Index Finger	|Escape|

### Right Hand

| Gesture | Action |
|---|---|
|Index + Middle | Right Arrow|
|Thumb|	Space|
|Index Finger|	F5 / Refresh|

---

# Changing the Active Profile

The keyboard profile is configured in:
```
src/config.py
```
To use the default profile:
```
KEYBOARD_PROFILE = "default"
```
To use the presentation profile:
```
KEYBOARD_PROFILE = "presentation"
```
Restart the application after changing the profile.

---

# Gesture Recognition Reference

The gesture detector represents finger states in the following order:
```
[Thumb, Index, Middle, Ring, Pinky]
```
Examples:

|Finger State|	Gesture|
|--|--|
|[1, 0, 0, 0, 0]|	Thumb|
|[0, 1, 0, 0, 0]|	Index Finger|
|[0, 1, 1, 0, 0]|	Index + Middle|

A value of:
```
1 → Finger raised
0 → Finger folded
```


# Safety Behavior

The controllers include several safety mechanisms.

### Mouse

- Click cooldown prevents rapid repeated clicks.
- Dragging stops when the gesture changes.
- Dragging stops if the hand disappears.
- Camera resources are released when the application exits.

### Keyboard
- Keyboard actions use a cooldown to prevent repeated triggering.
- Unknown gestures do not trigger configured actions.
- Actions are executed only when a valid hand and supported gesture are detected.

# Future Gesture Improvements

Potential future additions include:
- Double-click gesture.
- Right-click gesture.
- Scroll gesture.
- Additional mouse gestures.
- Custom keyboard gesture mappings.
- User-defined keyboard profiles.
- Gesture sensitivity settings.
- Debug mode for gesture detection.