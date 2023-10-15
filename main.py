import os
import pyautogui

# Locations of the respective buttons on the computer screen
SCAN_BUTTON = (900, 700)
MINIMIZE_BUTTON = (464, 127)


def auto_scan():
    """Opens the malwarebytes application, runs a virus scan, and minimizes the app when done."""
    os.system("open /Applications/Malwarebytes.app/")
    pyautogui.moveTo(SCAN_BUTTON)
    pyautogui.leftClick()
    pyautogui.moveTo(MINIMIZE_BUTTON)
    pyautogui.leftClick()


if __name__ == '__main__':
    initialMouseLocation = (pyautogui.position())
    auto_scan()
    pyautogui.moveTo(initialMouseLocation)
