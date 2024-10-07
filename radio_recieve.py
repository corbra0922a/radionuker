from microbit import *
import microbit
from radio import *
import radio
radio.on()
message=radio.receive()

while True:
    if message is not None:
        print(message)
        display.scroll(message)
        display.clear()
