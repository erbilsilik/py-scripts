import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.click(pyautogui.position(), button='right')
pyautogui.click(pyautogui.moveRel(24,220))
pyautogui.click(pyautogui.position(), button='left')
pyautogui.moveTo(73,78)
pyautogui.dragTo(80, 140, 0.5, button='left')
