import pyautogui
import time

# variables including: position, time, and duration.

x_pos = 300
y_pos = 400
x1_pos = 802
y1_pos = 629
wait_time = 3
run_time = 4200  # in seconds

start_time = time.time()
current_time = time.time()

# loops through varying in position for the duration specified.

while current_time - start_time < run_time:
    pyautogui.moveTo(x_pos, y_pos)
    time.sleep(wait_time)
    pyautogui.moveTo(x1_pos, y1_pos)
    pyautogui.doubleClick()
    time.sleep(wait_time)
    pyautogui.moveTo(y_pos, x1_pos)
    time.sleep(wait_time)
    pyautogui.moveTo(y1_pos, x_pos)
    time.sleep(wait_time)
    current_time = time.time()
