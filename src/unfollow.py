#!/usr/bin/env python3

import pyautogui
import time

pyautogui.useImageNotFoundException(False)

time.sleep(3)

icons = ["unfollow.png", "unfollow2.png"]

while True:
    found_any = False

    for icon in icons:
        location = pyautogui.locateOnScreen(icon, confidence=0.8)

        if location:
            found_any = True
            pyautogui.click(pyautogui.center(location))
            time.sleep(2)

    if not found_any:
        pyautogui.hotkey("ctrl", "r")
        time.sleep(5)

