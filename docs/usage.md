# Usage Guide

This guide explains how to run and use the Touchless Computer Control application.

## 1. Starting the Application

Activate the virtual environment if it is not already active.

### Windows

```powershell
.venv\Scripts\Activate.ps1
```
Run the application from the project root:
```
python main.py
```
The application displays a menu:
1. Virtual Mouse
2. Gesture Keyboard

Enter the number corresponding to the desired mode.

## 2. Virtual Mouse

Select:
```
1
```
A camera window named Virtual Mouse will open.

The application uses hand tracking to detect gestures and control the system cursor.

### Mouse Control

- The index fingertip is mapped to the screen position.
- Move your index finger to move the mouse cursor.

#### Click

- Bring the thumb and index fingertips close together.
```
Thumb + Index
      ↓
    Pinch
      ↓
 Left Mouse Click
```
A cooldown prevents repeated clicks from being triggered too quickly.

#### Drag

- Raise the index and middle fingers.
```
Index + Middle
       ↓
      Drag
```
The left mouse button remains pressed while the drag gesture is active.

When the gesture changes or the hand disappears, the mouse button is automatically released.

## 3. Gesture Keyboard

Select:
```
2
```
A camera window named Gesture Keyboard will open.

The application detects the hand, identifies the gesture, and maps it to a keyboard action based on the active keyboard profile.

The current status overlay displays information similar to:
```
Hand: Right
Gesture: Index + Middle
Action: Right Arrow
```
### Keyboard Gestures

The exact actions depend on the selected keyboard profile.

The default profile includes gestures such as:
```
Left Hand
├── Index + Middle → Left Arrow
├── Thumb → Space
└── Index → Alt + Tab

Right Hand
├── Index + Middle → Right Arrow
├── Thumb → Escape
└── Index → F5
```
More details about available controls are available in:

[Gesture Controls](controls.md)

## 4. Keyboard Profiles

The active keyboard profile is configured in:
```
src/config.py
```
For example:
```
KEYBOARD_PROFILE = "default"
```
The project currently includes:
```
default
presentation
```
To change profiles, modify:
```
KEYBOARD_PROFILE = "presentation"
```
Then restart the application.

## 5. Exiting the Application

Both controller windows can be closed in two ways.

### Method 1: Press Q

With the camera window selected, press: `Q`
### Method 2: Close the Camera Window

Click the `X` button in the camera window.

The application releases the camera and closes the MediaPipe resources before terminating.

## 6. Tips for Better Gesture Detection

For more reliable hand detection:
- Use adequate lighting.
- Keep your hand clearly visible to the camera.
- Avoid a heavily cluttered background when possible.
- Keep the hand within the camera frame.
- Avoid extremely fast movements.
- Maintain a reasonable distance from the camera.