# Future Work

This document describes potential future improvements for the Touchless Computer Control project.

The current version provides working Virtual Mouse and Gesture Keyboard modes. Future development can focus on additional gestures, improved reliability, customization, testing, and user experience.

---

# Mouse Improvements

## Double-Click Gesture

Add a dedicated gesture for triggering a double-click.

Possible implementation:

```text
Gesture
   ↓
Double-Click Detection
   ↓
pyautogui.doubleClick()
```
## Right-Click Gesture

Add a gesture specifically for right-click functionality.

This would provide more complete mouse control without requiring a physical mouse.

## Scroll Gesture

Add vertical scrolling using a dedicated hand gesture.

Possible approach:
```
Two-Finger Gesture
       +
Vertical Hand Movement
       ↓
pyautogui.scroll()
```

## Adaptive Cursor Smoothing

Currently, cursor smoothing uses a fixed configuration value.

A future version could dynamically adjust smoothing based on hand movement speed:
```
Slow Movement
      ↓
Higher Precision

Fast Movement
      ↓
Faster Cursor Response
```

## Configurable Camera Selection

Allow users to select a camera device instead of always using the default camera.

For example:
```
Available Cameras

1. Integrated Webcam
2. USB Webcam

Select Camera:
```

## Mouse Gesture Debug Mode

Add an optional debug mode displaying:

- Hand landmarks.
- Finger states.
- Pinch distance.
- Click threshold.
- Drag detection state.
- Cursor coordinates.
- FPS.

This would simplify gesture calibration and troubleshooting.

# Keyboard Improvements

## Advanced Safety Controls

Add additional safeguards to prevent accidental system actions.

Possible features:

- Confirmation gestures for critical actions.
- Emergency gesture disable.
- Temporary controller pause.
- Configurable safe zones.
- Action lock/unlock mode.

## Improved Cooldown Handling

The current keyboard controller uses a general action cooldown.

Future versions could support:

- Per-action cooldowns.
- Per-gesture cooldowns.
- Configurable repeat behavior.
- Hold-to-repeat actions.

For example:
```
Left Arrow
Cooldown: 0.3 seconds

F5
Cooldown: 1.0 second
```

## Enhanced No-Hand and Unknown Gesture Handling

Improve feedback when:

- No hand is detected.
- An unsupported gesture is detected.
- A gesture changes rapidly.
- Hand detection confidence is low.

Possible status overlay:
```
Hand: Not Detected
Gesture: None
Action: Waiting
```

## Keyboard Debug Mode

Add an optional keyboard debugging overlay showing:

- Detected hand.
- Raw finger states.
- Recognized gesture.
- Active keyboard profile.
- Selected action.
- Cooldown status.

Example:
```
Hand: Right
Finger State: [0, 1, 1, 0, 0]
Gesture: Index + Middle
Profile: Default
Action: Right Arrow
Cooldown: Ready
```

## Extended Keyboard Profiles

Add additional predefined profiles such as:
```
default
presentation
media
browser
custom
```
Possible use cases:

## Media Profile
```
Gesture → Play/Pause
Gesture → Volume Up
Gesture → Volume Down
Gesture → Next Track
Gesture → Previous Track
```
## Browser Profile
```
Gesture → Back
Gesture → Forward
Gesture → Refresh
Gesture → New Tab
```
---

# Gesture Customization

Allow users to define their own gesture-to-action mappings.

For example:
```json
{
    "custom": {
        "Left": {
            "thumb": "space",
            "index": "ctrl+c"
        },
        "Right": {
            "thumb": "esc",
            "index": "ctrl+v"
        }
    }
}
```
A future version could load custom profiles from a JSON or YAML configuration file.

# User Interface

## Graphical User Interface

Add a GUI for:

- Selecting Mouse or Keyboard mode.
- Selecting camera devices.
- Choosing keyboard profiles.
- Configuring gestures.
- Adjusting sensitivity.
- Starting and stopping controllers.

Possible implementation options:
- Tkinter.
- PySide.
- CustomTkinter.

## Settings Management

Move configurable values from Python source code into an external configuration file.

Possible structure:
```
config/
├── mouse.json
├── keyboard.json
└── profiles.json
```

This would allow configuration changes without modifying application code.

# Performance Improvements

Future optimization could include:

- FPS monitoring.
- Reduced frame processing overhead.
- Adaptive frame resolution.
- Frame skipping.
- More efficient MediaPipe processing modes.
- Performance profiling.

# Testing Improvements

Expand automated testing to include:

- Keyboard action mapping.
- Keyboard profiles.
- Mouse gesture recognition.
- Handedness correction.
- Gesture state transitions.
- Cooldown behavior.
- Mocked PyAutoGUI actions.
- Controller integration tests.

## Continuous Integration

Add GitHub Actions to automatically run tests.

Example workflow:
```
Push / Pull Request
        ↓
GitHub Actions
        ↓
Install Dependencies
        ↓
Run Pytest
        ↓
Report Results
```

# Documentation Improvements

Future documentation additions could include:

- Demonstration screenshots.
- Animated GIFs showing gestures.
- Video demonstrations.
- API documentation.
- Gesture calibration guide.
- Troubleshooting guide.
- Development contribution guide.

# Packaging and Distribution

The application could eventually be packaged for easier use.

Possible options include:

- PyInstaller executable.
- Windows installer.
- Cross-platform application package.

The goal would be to allow users to run the application without manually setting up a Python environment.