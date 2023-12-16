import pyautogui
import time

pyautogui.moveTo(150, 1052) 
pyautogui.click()
pyautogui.moveTo(55,150)
pyautogui.click()
time.sleep(1)
pyautogui.write("github", interval=0.1)
pyautogui.press('enter')
pyautogui.moveTo(200,320)
time.sleep(0.5)
pyautogui.click()
