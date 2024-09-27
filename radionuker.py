from microbit import *
import radio
import microbit
# Initialize the radio
radio.on()

# Message to send
message = 'NUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKED'

while True:
    display.scroll('NUKE MODE')
    for group in range(1, 256):  # Groups from 1 to 256
        radio.config(group=group)
        radio.send(message)
        print(str(group))
        sleep(1)
