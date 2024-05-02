from gpiozero import RGBLED, Button
import time
import random
from signal import pause

LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(23)
red_color = (1, 0, 0)
green_color = (0, 1, 0)
blue_color = (0, 0, 1)
is_red = False
is_green = False
is_blue = False
game_over = False

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def generate_color():
    global red_color, green_color, blue_color, is_red, is_green, is_blue
    colors = [red_color, green_color, blue_color]
    
    chosen_color = random.choice(colors)
    
    if chosen_color == red_color:
        print("Red!")
        is_red = True
        is_green = False
        is_blue = False
    elif chosen_color == green_color:
        print("Green!")
        is_green = True
        is_red = False
        is_blue = False
    else:
        print("Blue!")
        is_blue = True
        is_green = False
        is_red = False    
    
    return chosen_color

def color_check():
    global green_color, red_color, game_over
    
    game_over = True
    if is_green == True:
        print("\n-- You win! --")
        for i in range(5):
            set_color(0, green_color[1], 0)
            time.sleep(0.3)
            set_color(0, 0, 0)
            time.sleep(0.3)
            i = i + 1
    else:
        print("\n-- You Lose! You react as fast as a snail. --")
        for i in range(5):
            set_color(red_color[0], 0, 0)
            time.sleep(0.3)
            set_color(0, 0, 0)
            time.sleep(0.3)
            i = i + 1
        
        

def end_program():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ("-- LED Program On --")
    try:
        BUTTON.when_pressed = color_check
        while not game_over:
            random_color = generate_color()
            set_color(random_color[0], random_color[1], random_color[2])
            time.sleep(0.5)
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        end_program()