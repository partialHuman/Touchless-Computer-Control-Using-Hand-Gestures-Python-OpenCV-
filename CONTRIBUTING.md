# Contributing to Touchless Computer Control

Thank you for your interest in contributing to this project!

This project is an educational and experimental touchless computer control system built using Python, OpenCV, MediaPipe, and PyAutoGUI.

Contributions that improve functionality, reliability, documentation, testing, or usability are welcome.

---

## Table of Contents

1. [How to Contribute](#how-to-contribute)
2. [Development Guidelines](#development-guidelines)
3. [Testing](#testing)
4. [Documentation](#documentation)
5. [Commit Guidelines](#commit-guidelines)
6. [Pull Requests](#pull-requests)
7. [Areas for Contribution](#areas-for-contribution)
8. [Code of Conduct](#code-of-conduct)

---

## How to Contribute

### 1. Fork the Repository

Create your own fork of the repository on GitHub.

### 2. Clone Your Fork

```bash
git clone https://github.com/partialHuman/Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-.git

cd Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-
```
### 3. Create a Virtual Environment

For Windows:
```
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```
### 4. Install Dependencies
```
pip install -r requirements.txt
```
### 5. Create a Feature Branch

Use a descriptive branch name:
```
git checkout -b feature/gesture-scroll
```
Examples:
```
feature/gesture-scroll
feature/right-click
fix/hand-detection
docs/improve-installation
test/keyboard-actions
```

## Development Guidelines

### Code Style
When contributing code:
- Follow standard Python conventions.
- bUse meaningful variable and function names.
- Keep functions focused on a single responsibility.
- Keep modules focused on a clear purpose.
- Avoid unnecessary code duplication.
- Add comments where the logic is not immediately clear.
- Prefer readable and maintainable code over overly complex solutions.

Example:
```py
def calculate_distance(point1, point2):
    """Calculate the distance between two points."""
```
Avoid unclear names such as:
```py
def calc(a, b):
    pass
```

### Keep the Architecture Modular

The project separates responsibilities into different modules.

For example:
- Hand detection belongs in `hand_tracker.py`.
- Gesture interpretation belongs in `gesture_detector.py`.
- Mouse control belongs in `mouse_controller.py`.
- Keyboard control belongs in `keyboard_controller.py`.
- Keyboard action execution belongs in `keyboard_actions.py`.
- Configuration values belong in `config.py`.

Try to reuse existing components instead of duplicating functionality.

### Project Structure

Keep new code organized according to the existing structure:
```
Touchless-Computer-Control-Using-Hand-Gestures-Python-OpenCV-
│
├── docs/
│   ├── architecture.md
│   ├── controls.md
│   ├── future-work.md
│   ├── installation.md
│   ├── testing.md
│   └── usage.md
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
├── CONTRIBUTING.md
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

When adding new functionality:

- Add source code to src/.
- Add tests to tests/.
- Add or update documentation in docs/.
- Add configurable values to src/config.py when appropriate.

## Testing

Before submitting changes, run:
```
pytest -v
```
Or:
```
pytest tests/
```
New logic should include tests whenever practical.

Examples of functionality that should be tested:
- Gesture recognition.
- Finger-state detection.
- Keyboard action mapping.
- Keyboard profiles.
- Cooldown behavior.
- Handedness correction.
- Gesture state transitions.

Also manually test features that interact with:

- Webcam input
- Hand detection
- Mouse control
- Keyboard actions

Ensure that existing functionality continues to work.


## Documentation

If your contribution changes how the project works, update the relevant documentation.

Examples:
| Change                 | Documentation          |
| ---------------------- | ---------------------- |
| New gesture            | `docs/controls.md`     |
| Installation changes   | `docs/installation.md` |
| Usage changes          | `docs/usage.md`        |
| Architecture changes   | `docs/architecture.md` |
| New tests              | `docs/testing.md`      |
| Planned future feature | `docs/future-work.md`  |

The `README.md` should remain a concise project overview.

Detailed documentation should generally be placed inside the `docs/` directory.

## Commit Guidelines

Use clear and descriptive commit messages.

Recommended prefixes:
```
feat: add new functionality
fix: resolve a bug
docs: update documentation
test: add or update tests
refactor: restructure existing code
chore: maintenance changes
```
Examples:
```
feat: add scroll gesture
fix: release drag when hand disappears
docs: improve usage guide
test: add keyboard action tests
```

## Pull Requests

Before opening a pull request:

1. Ensure the project runs successfully.
2. Run the automated tests.
3. Update relevant documentation.
4. Add tests for new logic when possible.
5. Keep changes focused on a single feature or fix.

In the pull request description, explain:

- What was changed.
- Why the change was needed.
- How the feature was tested.
- Any limitations or known issues.

Example:
```markdown
## Description

Briefly describe the changes.

## Changes Made

- Change 1
- Change 2

## Testing

- [ ] Automated tests passed
- [ ] Manual testing completed

## Additional Notes

Include any limitations, known issues, or future improvements.
```

## Areas for Contribution

Potential contribution areas include:

- New mouse gestures
- Scroll support
- Right-click and double-click gestures
- Additional keyboard profiles
- Custom gesture mappings
- Gesture configuration files
- User interface development
- Improved testing
- GitHub Actions CI
- Performance optimization
- Application packaging

For the current roadmap, see: [docs/future-work](/docs/future-work.md)

## Reporting Issues
When reporting a bug, please include:
- Operating system.
- Python version.
- Steps to reproduce the issue.
- Expected behavior.
- Actual behavior.
- Error messages or traceback.
- Relevant screenshots, if applicable.

Example:
```markdown
Operating System: Windows 11
Python Version: 3.11

Steps to Reproduce:
1. Start Virtual Mouse mode.
2. Raise Index + Middle fingers.
3. Remove hand from camera.

Expected:
Mouse button should be released.

Actual:
Drag remains active.

Error:
No error message displayed.
```
## Code of Conduct

Please be respectful and constructive when contributing to the project.

#### Contributors are encouraged to:
- Provide constructive feedback.
- Respect different experience levels.
- Keep discussions focused on improving the project.
- Be welcoming to new contributors.
- Report issues clearly and respectfully.

The goal is to maintain a collaborative environment for learning, experimentation, and project improvement..


## Thank You

Thank you for contributing to Touchless Computer Control Using Hand Gestures.

Your contributions, whether they involve code, testing, documentation, bug reports, or ideas, help improve the project and make it more useful for others.

```markdown
Save this as:

```text
CONTRIBUTING.md
```

Then commit it:

```powershell
git add CONTRIBUTING.md
git commit -m "docs: add contributing guidelines"
```

---