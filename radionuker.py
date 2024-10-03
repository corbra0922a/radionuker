from microbit import *
import radio
import microbit

    #I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
    #ValueError: value out of range for argument 'channel'
    #I think it's because the microbit only has 84 channels


message='HI'
while True:
    #1 through 84
    for i in range (1,84):
        #sets the radio channel to the value of i
        radio.config(channel=i)
        #sends the variable 'message'
        radio.send(message)
        sleep(5)
