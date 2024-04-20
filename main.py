# #7c131e
# 750 720
# 905 1011

from pynput import keyboard
from pynput import mouse
from PIL import ImageGrab
import time



def isRed(rgb, tolerance=200):
    # rgb is a tuple containing (R, G, B) values
    r, g, b = rgb
    
    # Define the range of red shades based on tolerance
    red_min = 255 - tolerance
    red_max = 255

    
    
    # Check if the color falls within the range of red shades
    return r >= red_min and r <= red_max and g < 70 and b < 70

def getColor(x, y):
    bbox = (x, y, x+1, y+1)
    im = ImageGrab.grab(bbox = bbox)
    r, g, b =im.getpixel((0, 0))
    return((r, g, b))

def press(x):
    keyboard.Controller().press(x)
def release(x):
    keyboard.Controller().release(x)

time.sleep(1)

press('s')
while(True):
    time.sleep(0.1)
    if(isRed(getColor(750, 720))):
        keyboard.Controller().tap('f')
        print('Pressed F')
        time.sleep(0.1)
        if(getColor(905, 1011) == (44, 92, 252)):
            keyboard.Controller().tap('f')
        else:
            time.sleep(0.9)
            keyboard.Controller().tap('f')

