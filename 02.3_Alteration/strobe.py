from gpiozero import LED as LEDClass, Button
from signal import pause
import time

LED = LEDClass(17)
BUTTON = Button(18)
flashing = False

def flash():
     global LED, flashing
     if flashing:
             LED.toggle()
             time.sleep(0.1)
     else:
         LED.off()
     
def change_state():
    global flashing
    if flashing == False:
        flashing = True
    else:
        flashing = False
    if flashing:
         print("\n**Flash is on!**")
    else:
         print("\n..Flash deactivated..")
        
def end_program():
    LED.close()
    BUTTON.close()

if __name__ == "__main__":
    print("-- Program Started --")
    
    try:
        BUTTON.when_pressed = change_state
        while True:
            flash()
    except KeyboardInterrupt:
        end_program()