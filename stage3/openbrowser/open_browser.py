import webbrowser
import time

NUM_BREAKS = 3
MINS_BETWEEN_BREAKS = 120

n = 0
while n < NUM_BREAKS:
    time.sleep(MINS_BETWEEN_BREAKS)
    webbrowser.open("http://www.google.com")
    n += 1