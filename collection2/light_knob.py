# Description : Control RGBLED with Potentiometers
from pathlib import Path
import sys
from gpiozero import LED
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False

RED_LED = LED(27) 
GREEN_LED = LED(17)
BLUE_LED = LED(18)
YELLOW_LED = LED(23)
ADC = ADCDevice() # Define an ADCDevice class object



def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    
def loop():
    global ADC
    while True:     
        value = ADC.analogRead(0)
        
        blue_min = 0.25
        green_min = 0.5
        yellow_min = 0.75
        red_min = 0.95
                
        if (value / 255.0) >= blue_min and (value / 255.0) < green_min:
            BLUE_LED.on()
            GREEN_LED.off()
            YELLOW_LED.off()
            RED_LED.off()
        elif (value / 255.0) >= green_min and (value / 255.0) < yellow_min:
            BLUE_LED.on()
            GREEN_LED.on()
            YELLOW_LED.off()
            RED_LED.off()
        elif (value / 255.0) >= yellow_min and (value / 255.0) < red_min:
            BLUE_LED.on()
            GREEN_LED.on()
            YELLOW_LED.on()
            RED_LED.off()
        elif (value / 255.0) >= red_min:
            BLUE_LED.on()
            GREEN_LED.on()
            YELLOW_LED.on()
            RED_LED.on()
        else:
            BLUE_LED.off()
            GREEN_LED.off()
            YELLOW_LED.off()
            RED_LED.off()
        
        # print read ADC value
        print(f'Potentiometer Value: {value / 255.0}')
        time.sleep(0.01)

def destroy():
    global ADC, LED
    ADC.close()
    LED.close()
    
if __name__ == '__main__': # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()