# Run 'pip install pyautogui' before running this script

from pyautogui import press, typewrite, hotkey
import time

def countdown(t):
    print('Select window to pipe text to\n')
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Inputting Text...\n')

countdown(5)

# Simulate an individual keypress
#press('a')

# Simulate typing a block of text
typewrite('test')

#hotkey('ctrl', 'w')