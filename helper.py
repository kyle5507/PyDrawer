import time

import mouse
import pyautogui
from PIL import Image


def drawColor(im, color, offx, offy):
    px = im.load()
    ##click middle for color
    for x in range(im.width):
        for y in range(im.height):
            if px[x, y] == color:
                mouse.move(x + offx, y + offy)
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


def imageToPallet(im):
    PALETTE = [
        0, 0, 0,  # black,  00
        255, 255, 255,  # green,  01
        # 255, 0, 0,  # red,    10
        # 255, 255, 0,  # yellow, 11
    ]

    # a palette image to use for quant
    pimage = Image.new("P", (1, 1), 0)
    pimage.putpalette(PALETTE)

    # open the source image
    image = im.convert("RGB")

    # quantize it using our palette image
    imagep = image.quantize(palette=pimage)
    return imagep


# Create a Primary Colors version of the image
def convert_primary(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = image
    pixels = new.load()

    # Transform to primary
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = pixels[i, j]

            # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # Transform to primary
            if red > 127:
                red = 255
            else:
                red = 0
            if green > 127:
                green = 255
            else:
                green = 0
            if blue > 127:
                blue = 255
            else:
                blue = 0

            # Set Pixel in new image
            pixels[i, j] = (int(red), int(green), int(blue))

    # Return new image
    return new
