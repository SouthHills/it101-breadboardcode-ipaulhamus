from gpiozero import Button
from signal import pause
import time
import subprocess

BUTTON = Button(18)
BUTTON2 = Button(20)
chrome_active = False
chrome_process_id = None
fox_active = False
fox_process_id = None


def fox_function():
     global fox_active, fox_process_id
     if fox_active == False:
        fox_active = True
        print("--Firefox on--")
        fox_process_id = subprocess.Popen(["firefox"])
     else:
        fox_active = False
        print("--Firefox off--")
        fox_process_id.terminate()
        
def chrome_function():
     global chrome_active, chrome_process_id
     if chrome_active == False:
        chrome_active = True
        print("--Chrome on--")
        chrome_process_id = subprocess.Popen(["chromium-browser"])
     else:
        chrome_active = False
        print("--Chrome off--")
        chrome_process_id.terminate()
        
def end_program():
    BUTTON.close()

if __name__ == "__main__":
    print("-- Program Started --")
    try:
        while True:
            BUTTON.when_pressed = fox_function
            BUTTON2.when_pressed = chrome_function
    except KeyboardInterrupt:
        end_program()