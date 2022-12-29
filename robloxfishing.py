import pyautogui
import time
import keyboard
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(950, 300) == (40, 0, 159):
        time.sleep(0.28)
        keyboard.press_and_release('e')
        time.sleep(1)