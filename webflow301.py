import pyautogui
import time
import pyperclip

time.sleep(2)
with open('YOUR_TEXTFILE.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
for i in range(len(content)):
    skrive = str(content[i])
    pyperclip.copy(skrive)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('/')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=2, interval=0.25)
    pyautogui.keyUp('shift')
    time.sleep(1)