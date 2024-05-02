from gpiozero import LED
import time

redLED = LED(17)  # define led
greenLED = LED(27)
yellowLED = LED(13)

def loop():
    while True:
        yellowLED.off()
        redLED.on() 
        print ("\nRed light!")
        time.sleep(5)
        greenLED.on()
        redLED.off()
        print("\nGreen light! Go!")
        time.sleep(7)
        yellowLED.on()
        greenLED.off()
        print("\nYellow light! Slow down!")
        time.sleep(2)
        
        
def destroy():
    LED.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()