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
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=3, interval=0.25)
    pyperclip.copy('/')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab', presses=2, interval=0.25)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyDown('shift')
    pyautogui.press('tab', presses=5, interval=0.25)
    pyautogui.keyUp('shift')
    time.sleep(1)