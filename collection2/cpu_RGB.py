from gpiozero import RGBLED
import time
import random
import subprocess

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=5, green=6, blue=13, active_high=True)

temp_values = (10, 20, 30, 40, 50, 60, 70, 80)
red_temp_scale = (0.125, 0.250, 0.375, 0.5, 0.625, 0.750, 0.875, 1)
blue_temp_scale = (1, 0.875, 0.750, 0.625, 0.5, 0.375, 0.250, 0.125)

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def initial_test():
    set_color(1, 0, 0)
    print("All red")
    time.sleep(1)
    set_color(0, 1, 0)
    print("All green")
    time.sleep(1)
    set_color(0, 0, 1)
    print("All blue")
    time.sleep(1)

#def loop():
    #while True:
        #r=random.randint(0,100)
        #g=random.randint(0,100)
        #b=random.randint(0,100)
        #set_color(r / 100, g / 100, b / 100) # Colors should be between 0 and 1
       #print (f'r={r}% \tg={g}% \tb={b}%')
        
        #f = open("/sys/class/thermal/thermal_zone0/temp")
        
def temp_loop():
    while True:
        red_value = 0
        blue_value = 0
        
        f = open("/sys/class/thermal/thermal_zone0/temp")
        cpu_temp = float(f.read()) / 1000
        print(float(cpu_temp))
        time.sleep(1)
        
        
        
        
def destroy():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        temp_loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()