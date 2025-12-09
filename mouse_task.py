import pyautogui


def tracker():
    x, y = pyautogui.position()
    return x, y


def main():
    x, y = tracker()
    print(f"Mouse position: X={x}, Y={y}")


if __name__ == "__main__":
    main()
