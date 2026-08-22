import cv2

from src.mouse_controller import MouseController
from src.keyboard_controller import KeyboardController


def show_menu():
    print("\n" + "=" * 45)
    print("     TOUCHLESS COMPUTER CONTROL")
    print("=" * 45)
    print("1. Virtual Mouse")
    print("2. Gesture Keyboard")
    print("3. Exit")
    print("=" * 45)


def main():
    while True:
        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            mouse = MouseController()
            mouse.run()

        elif choice == "2":
            keyboard = KeyboardController()
            keyboard.run()

        elif choice == "3":
            print("Exiting Touchless Computer Control...")
            cv2.destroyAllWindows()
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()