import pyautogui
import time

time.sleep(5)

with open('script.txt', 'r') as f:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')

        