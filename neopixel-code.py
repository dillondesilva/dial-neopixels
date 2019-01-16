from microbit import *
import neopixel
import radio

radio.on()
radio.config(channel=21)

neopixels = neopixel.NeoPixel(pin13, 12)

while True:
    msg = radio.receive()
    if msg:
        brightness_factor = float(msg) / 45
        print(msg)
        for n in range(len(neopixels)):
            neopixels[n] = (int(brightness_factor * 255),0,0)
        neopixels.show()