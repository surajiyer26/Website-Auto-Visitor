import webbrowser
import time
import keyboard

count = 15 # number of times you want to open a tab
secs = 1.5 # time after which a tab is to be closed

url = 'https://www.linkedin.com/in/suraj-iyer-524342228/'

for _ in range (count):
    # opens a new tab
    webbrowser.open(url, new=0)
    # closes the tab after some time
    time.sleep(secs)
    keyboard.press_and_release('Ctrl + W')
