from microbit import *
import radio
import microbit

message='NUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKEDNUKED'

while True:
    for i in range (1,99):
        radio.config(channel=i)
        radio.send(message)
        print('group',(i),('nuked'))
        sleep(10)
        
