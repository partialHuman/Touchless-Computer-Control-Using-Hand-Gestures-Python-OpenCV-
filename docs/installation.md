# Installation Guide

This guide explains how to set up and run the Touchless Computer Control project.

## Prerequisites

Before installing the project, make sure you have:

- Python 3.11 or newer
- A working webcam
- Git
- pip

> Python 3.11 is recommended for compatibility with the project dependencies.

---

## 1. Clone the Repository

Clone the repository:

```bash
git clone https://github.com/partialHuman/Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-.git
```
Move into the project directory:
```bash
cd Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-
```

## 2. Create a Virtual Environment

Create a virtual environment:

Windows
```bash
py -3.11 -m venv .venv
```
Activate it:
```bash
.venv\Scripts\Activate.ps1
```
Linux / macOS
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```
After activation, the terminal should show something similar to:
`(.venv)`

## 3. Install Dependencies

Install all required Python packages:
```bash
pip install -r requirements.txt
```
## 4. Verify the Installation

Check the Python version:
```bash
python --version
```
You can also verify MediaPipe:
```bash
python -c "import mediapipe as mp; print(mp.__version__)"
```

## 5. Verify the Hand Landmark Model

The project requires the MediaPipe hand landmark model:
```
models/
└── hand_landmarker.task
```
Make sure this file exists before running the application.

The model path is configured through:
```
src/config.py
```

## 6. Run the Application

Start the application from the project root:
```bash
python main.py
```
You should see a menu similar to:
```
1. Virtual Mouse
2. Gesture Keyboard
```
Select the desired mode and press Enter.

## Troubleshooting
### MediaPipe Import or Compatibility Issues

If you encounter MediaPipe-related errors, verify that you are using the project's virtual environment:
```bash
.venv\Scripts\Activate.ps1
```
Then check:
```bash
python --version
pip show mediapipe
```
Python 3.11 is recommended for the most reliable compatibility.

### Camera Cannot Be Opened

Make sure:
- Your webcam is connected.
- No other application is currently using the camera.
- Camera permissions are enabled.
- The correct camera device is available.

### PowerShell Blocks Virtual Environment Activation

If PowerShell blocks the activation script, you can allow local scripts for the current user:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then restart PowerShell and activate the environment again:
```bash
.venv\Scripts\Activate.ps1
```
