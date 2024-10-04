from microbit import *
import radio
import microbit

#turn on radio (duh)
radio.on()
#the radio message to send
radio_message='HI'
#'while True:' makes code loop forever (if it is true)
while True:
    #declares a variable named 'radio_group' then it will count in a range of 0 to 99 then it restarts
    for radio_group in range(0,99):
        #sets the group to the value of the 'radio_group' variable
        radio.config(group=radio_group)
        #sends the variable 'radio_message' (at the top)
        radio.send(radio_message)
        #I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
        #ValueError: value out of range for argument 'channel'
        #declares a variable named 'radio_channel' then it will count in a range of 0 to 84 then it restarts
        for radio_channel in range (0,84):
            #sets the radio channel to the value of i
            radio.config(channel=radio_channel)
            #sends the variable 'message'
            radio.send(radio_message)
            #sleep 1ms (you need it to sleep or else it will lag and be very slow)
            sleep(1)
            #prints the radio group you nuked then the channel you nuked (example below this comment)
            #group [group number] nuked channel [channel number] nuked
            print('group',radio_group,('nuked'),('channel'),(radio_channel),('nuked'))
        
