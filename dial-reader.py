from microbit import *
import radio

radio.on()
radio.config(channel=21)
while True:
    radio.send(str(pin0.read_analog()))