import pyautogui


class KeyboardActionExecutor:
    """Execute keyboard actions and shortcuts."""

    def execute(self, action):
        """
        Execute a configured keyboard action.

        Single key:
            "space"
            "left"
            "f5"

        Shortcut:
            "alt+tab"
            "ctrl+c"
            "ctrl+shift+s"
        """

        if not action:
            return False

        # Multi-key shortcut
        if "+" in action:
            keys = action.split("+")
            pyautogui.hotkey(*keys)

        # Single key
        else:
            pyautogui.press(action)

        print(f"Action: {action}")

        return True