from gpiozero import LED
import time

led = LED(17)  # define led
led2 = LED(27)

def loop():
    while True:
        led2.off()
        led.on() 
        print ("\nled1 turned on >>>") # print information on terminal
        time.sleep(1)
        led2.on()
        led.off()
        print ("\nled2 turned on <<<")
        time.sleep(1)
        
def destroy():
    # Release resources
    led.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {led.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
