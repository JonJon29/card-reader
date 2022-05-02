import board
import time
import neopixel

num_pixels = 12
pixels = neopixel.NeoPixel(board.D18, num_pixels)

def fadeInOut():
    color = [0, 0, 0]
    increment = 5 
    while True:
        color[0] += increment
        if color[0] >=255:
            color[0] = 255
            increment = -5
        if color[0] <= 0:
            color[0] = 0
            increment = 5 

        pixels.fill(color)
        pixels.write()
        time.sleep(0.01)

fadeInOut()
