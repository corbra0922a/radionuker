from microbit import *
import radio
import microbit

    #I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
    #ValueError: value out of range for argument 'channel'
    #I think it's because the microbit only has 84 channels
print('AWAITING COMMAND')
message='0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶'
start=0
while True:
    if start==1:
        
        #1 through 84
        for i in range (1,84):
            #sets the radio channel to the value of i
            radio.config(channel=i)
            #sends the variable 'message'
            radio.send(message)
            print('nuked channel',(i))
            sleep(5)
    if microbit.button_a.was_pressed():
        start=+1
        print('NUKE ONLINE :)')
        sleep(600)
        print('3')
        sleep(1000)
        print('2')
        sleep(1000)
        print('1')
        sleep(1000)
        print('NUKE MODE ACTIVE')
        sleep(500)
    if microbit.button_a.was_pressed():
        start=-1
        sleep(1000)
        print('nuke offline :(')
        
