import math

import pyautogui
import mouse
from PIL import Image, ImageGrab
import time

# using the grab method
im1 = ImageGrab.grab(bbox=None)
testimg = ImageGrab.grabclipboard()
testimg = testimg.resize((700, 700))


def drawColor(im, color, offx, offy):
    px = im.load()
    ##click middle for color
    for x in range(im.width):
        for y in range(im.height):
            if px[x, y] == color:
                mouse.move(x+offx,y+offy)
                mouse.click()
                time.sleep(0.001)


def ClickMiddle(minx, maxx, miny, maxy):
    middlex = (minx + maxx) / 2
    middley = (miny + maxy) / 2
    pyautogui.moveTo(middlex, middley)


def FindBounds(im):
    px = im.load()
    minx = im.width
    miny = im.height
    maxx = 0
    maxy = 0
    for x in range(im.width):
        for y in range(im.height):
            if px[x, y] == (246, 126, 74):
                if x < minx:
                    minx = x
                if y < miny:
                    miny = y
                if x > maxx:
                    maxx = x
                if y > maxy:
                    maxy = y
    return minx, maxy, maxx, miny


time.sleep(5)
drawColor(testimg, (0, 0, 0), 100, 100)
# im2 = ImageGrab.grab(bbox=(minx, miny, maxx, maxy))
# im2.show()
