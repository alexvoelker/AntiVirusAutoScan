import os
import pyautogui
import time
import psutil

# Locations of the respective buttons on the computer screen
SCAN_BUTTON = (900, 700)
MINIMIZE_BUTTON = (464, 127)
APP_NAME = "FrontendApplication" # Malwarebytes GUI appicatio is called 'Malwarebytes' on macOS.
SLEEP_TIME = 1.5 # sleep for time time in seconds after the app launches to give it time to open the GUI


def check_app_open(app_name: str, timeoutSeconds: int=10) -> bool:
    timeoutSeconds *= 1000000000 # seconds to nanoseconds
    currentTime = time.time_ns()

    while (time.time_ns() - currentTime < timeoutSeconds):
        if app_name in (i.name() for i in psutil.process_iter()):
            return True
    return False


def auto_scan():
    """Opens the malwarebytes application, runs a virus scan, and minimizes the app when done."""
    os.system("open /Applications/Malwarebytes.app/")
    check_app_open(APP_NAME)
    time.sleep(SLEEP_TIME)
    pyautogui.moveTo(SCAN_BUTTON)
    pyautogui.leftClick()
    pyautogui.moveTo(MINIMIZE_BUTTON)
    pyautogui.leftClick()


if __name__ == '__main__':
    initialMouseLocation = (pyautogui.position())
    auto_scan()
    pyautogui.moveTo(initialMouseLocation)

