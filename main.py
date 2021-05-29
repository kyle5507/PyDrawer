import math

import pyautogui
import mouse
from PIL import Image, ImageGrab
import time
from helper import *

# using the grab method
im1 = ImageGrab.grab(bbox=None)
testimg = ImageGrab.grabclipboard()

# time.sleep(5)
imageToPallet(testimg)
convert_primary(testimg).show()
# drawColor(testimg, (0, 0, 0), 100, 100)
# im2 = ImageGrab.grab(bbox=(minx, miny, maxx, maxy))
# im2.show()
