from microbit import *
import radio
import microbit

#I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
#ValueError: value out of range for argument 'channel'
#I think it's because the microbit only has 84 channels
radio.on()
radio_message='HI'
while True:           #1 through 10
    for radio_group in range(0,99):
        radio.config(group=radio_group)
        radio.send(radio_message)
                                #1 through 84
        for radio_channel in range (0,84):
            #sets the radio channel to the value of i
            radio.config(channel=radio_channel)
            #sends the variable 'message'
            radio.send(radio_message)
            #sleep 1ms (reduces lag alot)
            sleep(1)
            #prints the radio group you are in and the channel
            print('group',radio_group,('nuked'),('channel'),(radio_channel),('nuked'))
        
