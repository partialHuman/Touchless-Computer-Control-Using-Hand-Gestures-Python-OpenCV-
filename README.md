# Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-


## 📌 Overview
This project implements a real-time hand gesture recognition system using computer vision techniques to control mouse and keyboard operations without physical input devices.

Using a webcam, the system detects hand landmarks and interprets gestures to perform actions such as cursor movement, clicking, window switching, and keyboard shortcuts.

The project leverages MediaPipe for hand tracking, OpenCV for video processing, and PyAutoGUI for system automation.

---

## 🎯 Features

- Real-time hand detection and tracking  
- Virtual mouse movement using finger position  
- Mouse click using finger pinch gesture  
- Keyboard control using predefined hand gestures  
- No external hardware required (webcam only)  

---

## ⚙️ Technologies Used

- Python  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- CVZone Hand Tracking Module  
 

---

## ⌨️ Supported Gestures – Keyboard Control  

| Hand Used | Finger Pattern (Thumb → Pinky) | Action Performed |
|----------|-------------------------------|-----------------|
| Left Hand | 0 1 1 0 0 | Move Left Arrow |
| Left Hand | 1 0 0 0 0 | Space Bar |
| Left Hand | 0 1 0 0 0 | Alt + Tab |
| Right Hand | 0 1 1 0 0 | Move Right Arrow |
| Right Hand | 1 0 0 0 0 | Escape (Esc) |
| Right Hand | 0 1 0 0 0 | Refresh (F5) |

> Finger Pattern Format: [Thumb, Index, Middle, Ring, Pinky]

## 🖱️ Supported Gestures – Virtual Mouse  

| Gesture | Description | Action |
|--------|------------|-------|
| Index Finger Movement | Move index finger across screen | Cursor movement |
| Index + Thumb Close | Pinch gesture | Mouse click |
| Hand Tracking | Continuous landmark detection | Smooth pointer control |


---

## 📦 Required Libraries

Install using:

```bash
pip install -r requirements.txt
```

---

## ▶ How to Run

### Virtual Mouse:
```bash
python mouse.py
```

### Keyboard Control:
```bash
python HandGesture-Keyboard.py
```

---

## 🎛️ How to Customize Gestures  

You can easily modify or add new gestures by editing the finger pattern conditions in the Python scripts.

---

### ✋ For Keyboard Gestures (`HandGesture-Keyboard.py`)

Each gesture is detected using this pattern:

```python
fingers = detector.fingersUp(hand)
```

Example:

```python
if fingers == [0, 1, 1, 0, 0]:
    pyautogui.press("left")
```

#### ➕ To add a new gesture:

1. Print finger values:
```python
print(fingers)
```

2. Show a hand gesture and note the pattern

3. Add new condition:

```python
if fingers == [1, 1, 1, 0, 0]:
    pyautogui.press("volumeup")
```

---

### 🖱️ For Virtual Mouse (`mouse.py`)

Mouse actions are controlled by finger distance:

```python
if abs(index_y - thumb_y) < 20:
    pyautogui.click()
```

#### ➕ To change click sensitivity:

```python
if abs(index_y - thumb_y) < 40:   # more sensitive
```

or

```python
if abs(index_y - thumb_y) < 10:   # less sensitive
```

---

### 🎯 Tips for Better Accuracy

- Ensure good lighting  
- Keep hand inside camera frame  
- Avoid cluttered backgrounds  
- Use consistent hand gestures  


## 📈 Results

- Smooth real-time gesture tracking  
- Accurate hand landmark detection  
- Reliable system automation  
- Hands-free computer control  

---



## 🚀 Future Improvements

- Gesture customization  
- Multi-hand support  
- AI-based gesture classification  
- Mobile camera integration  
- Performance optimization  

