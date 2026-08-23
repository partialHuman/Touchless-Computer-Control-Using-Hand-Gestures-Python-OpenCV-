# Project Architecture

This document describes the architecture of the Touchless Computer Control system.

---

# System Overview

The project provides two computer-control modes:

1. [Virtual Mouse](#virtual-mouse-architecture)
2. [Gesture Keyboard](#gesture-keyboard-architecture)

Both modes share a common hand detection and gesture recognition pipeline.

```mermaid
flowchart TD

    A[Webcam Input] --> B[OpenCV Frame Capture]
    B --> C[HandTracker]

    C --> D[MediaPipe Hand Landmarker]
    D --> E[Hand Landmarks]
    E --> F[GestureDetector]

    F --> G{Selected Mode}

    G --> H[Virtual Mouse]
    G --> I[Gesture Keyboard]

    H --> J[PyAutoGUI Mouse Control]
    I --> K[KeyboardActionExecutor]

    K --> L[PyAutoGUI Keyboard Control]
```

---

# Project Structure

```
Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-
│
├── docs/
│   ├── installation.md
│   ├── usage.md
│   ├── controls.md
│   ├── architecture.md
│   ├── testing.md
│   └── future-work.md
│
├── models/
│   └── hand_landmarker.task
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── gesture_detector.py
│   ├── hand_tracker.py
│   ├── keyboard_actions.py
│   ├── keyboard_controller.py
│   └── mouse_controller.py
│
├── tests/
│   └── test_gesture_detector.py
│
├── .gitignore
├── main.py
├── README.md
├── report.pdf
└── requirements.txt
```

# Module Responsibilities

## 1. `main.py`

The application entry point.

#### Responsibilities:
- Display the controller selection menu.
- Start Virtual Mouse mode.
- Start Gesture Keyboard mode.

```mermaid
flowchart TD

    A[main.py] --> B{User Selection}

    B -->|1| C[MouseController]
    B -->|2| D[KeyboardController]
```

## 2. `src/config.py`

Contains centralized configuration values.

### Examples include:
- Camera dimensions.
- Hand detection confidence.
- Tracking confidence.
- Maximum number of hands.
- Mouse smoothing.
- Click threshold.
- Click cooldown.
- Keyboard action cooldown.
- Keyboard gesture definitions.
- Keyboard profiles.

This keeps configurable values separate from controller logic.

## 2. `src/hand_tracker.py`

Acts as the interface between the application and MediaPipe.

### Responsibilities:
- Convert OpenCV frames from BGR to RGB.
- Create MediaPipe image objects.
- Run hand landmark detection.
- Convert normalized landmarks into pixel coordinates.
- Determine hand type.
- Provide landmark information to controllers.
- Provide finger-state information.

### Hand Detection Flow

```mermaid
flowchart TD
    A[OpenCV Frame] --> B[BGR to RGB]
    B --> C[MediaPipe Image]
    C --> D[Hand Landmarker]
    D --> E[Hand Landmarks]
    E --> F[Pixel Coordinates]
    E --> G[Hand Type]
    E --> H[Finger States]
```

## 3. `src/gesture_detector.py`

Handles gesture interpretation.

It converts hand landmark information into finger states.

Finger state format: `[Thumb, Index, Middle, Ring, Pinky]`

For example:
```
[1, 0, 0, 0, 0] → Thumb
[0, 1, 0, 0, 0] → Index
[0, 1, 1, 0, 0] → Index + Middle
```
The gesture information is then used by the mouse and keyboard controllers.

---

# Virtual Mouse Architecture

The Virtual Mouse uses hand landmarks to control the system cursor.

```mermaid
flowchart TD

    A[Webcam] --> B[OpenCV]
    B --> C[HandTracker]

    C --> D[Hand Landmarks]

    D --> E[Index Fingertip]
    D --> F[Thumb Fingertip]
    D --> G[Finger States]

    E --> H[Screen Coordinate Mapping]
    H --> I[Cursor Smoothing]
    I --> J[PyAutoGUI moveTo]

    E --> K[Distance Calculation]
    F --> K
    K --> L{Pinch Detected?}
    L -->|Yes| M[Mouse Click]

    G --> N{Index + Middle?}
    N -->|Yes| O[Start Drag]
    N -->|No| P[Stop Drag]
```

## Mouse Gesture Processing

The mouse controller performs three primary functions:

### Cursor Movement
```
Index Fingertip
       ↓
Screen Coordinate Mapping
       ↓
Cursor Smoothing
       ↓
System Cursor Movement
```
### Click Detection
```
Thumb + Index
       ↓
Distance Calculation
       ↓
Below Click Threshold?
       ↓
Mouse Click
```
### Drag Detection

```
Index + Middle Raised
       ↓
Start Mouse Button Hold
       ↓
Gesture Ends
       ↓
Release Mouse Button
```

# Gesture Keyboard Architecture

The Gesture Keyboard converts recognized gestures into keyboard actions.

```mermaid
flowchart TD

    A[Webcam] --> B[HandTracker]

    B --> C[Hand Type]
    B --> D[Finger States]

    C --> E[KeyboardController]
    D --> E

    E --> F[Gesture Recognition]
    F --> G[Active Keyboard Profile]

    G --> H[Action Mapping]

    H --> I[KeyboardActionExecutor]

    I --> J{Action Type}

    J -->|Single Key| K[pyautogui.press]
    J -->|Shortcut| L[pyautogui.hotkey]

    K --> M[Keyboard Input]
    L --> M
```

## Keyboard Action Flow

```mermaid
sequenceDiagram

    participant C as Camera
    participant H as HandTracker
    participant G as GestureDetector
    participant K as KeyboardController
    participant P as Keyboard Profile
    participant E as KeyboardActionExecutor
    participant OS as Operating System

    C->>H: Frame
    H->>G: Hand landmarks
    G->>K: Hand type + finger states
    K->>P: Get mapped action
    P-->>K: Action

    K->>E: Execute action

    alt Single Key
        E->>OS: pyautogui.press()
    else Shortcut
        E->>OS: pyautogui.hotkey()
    end
```

## Keyboard Profiles

Keyboard actions are separated into configurable profiles.

```mermaid
flowchart TD

    A[Hand Type + Gesture] --> B{Active Profile}

    B --> C[Default]
    B --> D[Presentation]

    C --> E[Mapped Action]
    D --> E

    E --> F[KeyboardActionExecutor]
```
The active profile is configured in:
```
src/config.py
```
For example:
```
KEYBOARD_PROFILE = "default"
```
---

# Shared Gesture Pipeline

Both controller modes reuse the same detection components.
```mermaid
flowchart TD

    A[Camera Frame]
        --> B[HandTracker]

    B --> C[MediaPipe Detection]

    C --> D[Hand Landmarks]

    D --> E[GestureDetector]

    E --> F{Controller}

    F -->|Mouse Mode| G[MouseController]
    F -->|Keyboard Mode| H[KeyboardController]

    G --> I[Mouse Actions]
    H --> J[Keyboard Actions]
```
# Resource Cleanup

Both controllers perform cleanup when the application exits.
```mermaid
flowchart LR

    A[Exit: Q or Window Close]
        --> B[Stop Controller Loop]

    B --> C[Release Mouse Button if Dragging]

    C --> D[Release Camera]

    D --> E[Destroy OpenCV Windows]

    E --> F[Close HandTracker / MediaPipe]
```
This ensures that the webcam and MediaPipe resources are properly released when the program terminates.

---