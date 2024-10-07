from microbit import *
import radio
import microbit
mode=0
message='0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶'
print('button A=nuke')
print('button B=stop')
print('pin_logo=nuke with channel')
radio_message='HI'

while True:
    if mode==1:
        print('NUKE MODE ACTIVE')
        sleep(1000)
        print('press button B to stop')
        sleep(1500)
        #1 through 84
        for i in range (1,84):
            #sets the radio channel to the value of i
            radio.config(channel=i)
            #sends the variable 'message'
            radio.send(message)
            #print 'group' and 'i' and also adds the word 'nuked' at the end
            sleep(1)
    if microbit.button_a.was_pressed():
        mode=1
    if microbit.button_b.was_pressed():
        mode=0
    if pin_logo.is_touched():
        mode=2
    if mode==2:
            #declares a variable named 'radio_group' then it will count in a range of 0 to 99 then it restarts
            for radio_group in range(0,99):
                #sets the group to the value of the 'radio_group' variable
                radio.config(group=radio_group)
                #sends the variable 'radio_message' (at the top)
                radio.send(radio_message)
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
        
