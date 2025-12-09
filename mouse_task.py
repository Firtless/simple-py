import pyautogui
import time


def tracker():
    x, y = pyautogui.position()
    return x, y


def countdown(seconds):
    x, y = tracker()
    while seconds > 0:
        print(f"Mouse position: X={x}, Y={y}")
        print(seconds)
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("Time's up!")


countdown(10)


# def main():
#     x, y = tracker()
#     print(f"Mouse position: X={x}, Y={y}")


if __name__ == "__countdown__":
    countdown()
