from gpiozero import LED
import time
import subprocess

led = LED(17)  # define led
led2 = LED(27)

def loop():
    while True:
        if is_internet_connected():
            led.on()
            led2.off()
        else:
            led2.on()
            led.off()
        time.sleep(2)
        
def destroy():
    # Release resources
    led.close()
    
def is_internet_connected():
    try:
        subprocess.check_output(['ping', '-c', '1', '-w', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pins {led.pin}, {led2.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()