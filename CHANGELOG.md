# Changelog

All notable changes to **Touchless Computer Control Using Hand Gestures** will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows Semantic Versioning where practical.

---

## [Unreleased]

### Planned

- Double-click gesture.
- Right-click gesture.
- Scroll gesture.
- Adaptive cursor smoothing.
- Camera selection.
- Additional keyboard profiles.
- Custom gesture mappings.
- Debug modes.
- Expanded automated testing.
- GitHub Actions CI.
- GUI-based configuration.
- Application packaging and distribution.

---

## [1.0.0] - 2026-08-23

### Added

#### Virtual Mouse

- Index-finger-based cursor movement.
- Screen coordinate mapping.
- Cursor smoothing.
- Thumb and index pinch detection for left click.
- Click cooldown protection.
- Index and middle finger drag gesture.
- Automatic drag release when the gesture changes.
- Automatic drag release when the hand disappears.

#### Gesture Keyboard

- Left and right hand detection.
- Finger-state-based gesture recognition.
- Configurable keyboard action mappings.
- Support for single-key actions.
- Support for keyboard shortcuts.
- Keyboard action cooldown.
- Default keyboard profile.
- Presentation keyboard profile.
- Gesture and action status display.

#### Hand Tracking

- MediaPipe Hand Landmarker integration.
- OpenCV webcam capture.
- Hand landmark detection.
- Pixel coordinate conversion.
- Handedness processing.
- Finger-state detection.
- Shared hand tracking pipeline for both controllers.

#### Project Architecture

- Modular source code structure.
- Separate mouse and keyboard controllers.
- Dedicated gesture detector.
- Centralized configuration.
- Separate keyboard action handling.

#### Testing

- Automated gesture detector tests.
- Manual testing procedures.
- Regression testing checklist.

#### Documentation

- Installation guide.
- Usage guide.
- Gesture controls reference.
- Project architecture documentation.
- Mermaid workflow diagrams.
- Testing guide.
- Future work roadmap.
- Project report.
- Contributing guidelines.

#### Project Maintenance

- Improved `.gitignore`.
- Added project license.
- Organized documentation inside the `docs/` directory.
- Cleaned up repository structure.
- Improved README as the project landing page.

---

## [0.5.0]

### Added

- Gesture Keyboard controller.
- Left and right hand gesture mappings.
- Keyboard action cooldown.
- Keyboard profiles.
- Keyboard action execution using PyAutoGUI.

### Improved

- Gesture detection integration.
- Handedness handling.
- Controller cleanup behavior.

---

## [0.4.0]

### Added

- Virtual Mouse controller.
- Cursor movement using the index fingertip.
- Cursor smoothing.
- Pinch-based click detection.
- Click cooldown.
- Drag gesture using index and middle fingers.

### Improved

- Safe drag release behavior.
- Camera and MediaPipe resource cleanup.

---

## [0.3.0]

### Added

- Shared hand tracking system.
- MediaPipe Hand Landmarker integration.
- Hand landmark extraction.
- Pixel coordinate conversion.
- Finger-state detection.
- Gesture detection utilities.

---

## [0.2.0]

### Added

- Project restructuring.
- Modular source code organization.
- Centralized configuration.
- Improved controller separation.

---

## [0.1.0]

### Added

- Initial project setup.
- Python virtual environment configuration.
- OpenCV integration.
- MediaPipe setup.
- Basic webcam hand detection prototype.

---

## Version History

```text
0.1.0
  │
  ├── Initial Hand Detection
  │
0.2.0
  │
  ├── Project Restructure
  │
0.3.0
  │
  ├── Hand Tracking and Gesture Detection
  │
0.4.0
  │
  ├── Virtual Mouse
  │
0.5.0
  │
  ├── Gesture Keyboard
  │
1.0.0
  │
  └── Documentation and Project Release