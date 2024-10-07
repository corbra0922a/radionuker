from microbit import *
import radio
import microbit
#If mode=0 it just idles
#If mode=1 it starts the nuke
#If mode=2 it does radio channel and group nuke
#If mode=3 it stops everything and prints the controls
#If mode=4 controls
#If mode=5 controls
#If mode=6 it starts scanner
#If mode=7 controls

#I just relized I could have just had multiple varibles and have 1=on and 2=off instead of controlling one variable
#Im dumb



radio.on()
print('button A=nuke')
print('button B=stop everything')
print('pin_logo=nuke channel and group')
print('button A and button B (same time)=channel scan')
mode=0
message='0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶0̶'
radio_message='HI'

while True:
    if mode==1:
        #1 through 84
        for i in range (0,84):
            print('channel',(i),'nuked')
            #sets the radio channel to the value of i
            radio.config(channel=i)
            #sends the variable 'message'
            radio.send(message)
            #print 'group' and 'i' and also adds the word 'nuked' at the end
            sleep(1)
    if microbit.button_a.was_pressed():
        mode=1
    if microbit.button_b.was_pressed():
        mode=3
    if pin_logo.is_touched():
        mode=2
  
    if button_a.was_pressed() and button_b.was_pressed():
        mode=7
        break
        
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
    
    if mode==3:
        print('button A=nuke')
        print('button B=stop everything')
        print('pin_logo=nuke channel and group')
        print('press button A and B (same time) starts the channel scanner')
        print('button A and button B (same time)=channel scan')
        sleep(1000)
        mode=0
    if mode==4:
        print('channel nuke')
        sleep(1000)
        print('press button B to stop')
        sleep(1500)
        mode=1
    if mode==5:
            print('radio channel and group nuke')
            sleep(1000)
            print('press button B to stop')
            sleep(1000)
            mode=2
    if mode==6:
        while True:
             for scanner in range(0,84):
                 radio.config(channel=scanner)
                 print('nothing',('found'),('in channel'),(scanner))
                 sleep(1)
    if mode==7:
            print('scanner mode')
            sleep(1000)
            print('press button B to stop')
            sleep(1000)
            mode=6

