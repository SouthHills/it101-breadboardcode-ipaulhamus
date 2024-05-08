# Description : Control LED with Photoresistor
from pathlib import Path
import sys
from gpiozero import LEDBarGraph
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED = LEDBarGraph(18, 23, 24, 25, 12, 16, 20, 21, 17, 13)

led_values = (0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0)
value_scale = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

ADC = ADCDevice() # Define an ADCDevice class objec

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

def graph_loop():
    global ADC, LED, led_values, value_scale
    while True:
        value = ADC.analogRead(0)
        voltage = value / 255.0 * 3.3
        
        for i in range(9):
            if value >= value_scale[i]:
                LED.value = led_values[i]
        
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tLED Value: {LED.value:.2f}')
    

def destroy():
    global ADC, LED
    ADC.close()
    LED.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        graph_loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
