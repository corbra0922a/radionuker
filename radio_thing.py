from microbit import *
import radio
import microbit

    #I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
    #ValueError: value out of range for argument 'channel'
    #I think it's because the microbit only has 84 channels
print('pinlogo=scanner mode')
sleep(200)
print('Button A=start nuker')
sleep(200)
print('Button B=stop nuker')
        
message='Hello :)'
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
    if microbit.button_b.was_pressed():
        start=-1
        sleep(1000)
        print('nuke offline :(')
        print('pinlogo=scanner mode')
        sleep(200)
        print('Button A=start nuker')
        sleep(200)
        print('Button B=stop nuker')
    if microbit.pin_logo.is_touched():
        start=+3
    if start==3:
        print('scan mode active')
        sleep(2000)
        print('shake microbit to go back to nuke')
        message=radio.receive()
        radio_message=('.,-')
        while True:
             for scanner in range(0,84):
                radio.config(channel=scanner)
                print('nothing',('found'),('in group'),(scanner))
                sleep(1)
                if message is not None:
                     print(message,('sent from channel',(scanner),))
                     sleep(1000)
                     radio.send(radio_message)
                     print('sent message to channel',(scanner))
                     sleep(200)
    if button_a.is_pressed() and button_b.is_pressed():
        start=+4
        
    if start==4:
        print('pinlogo=scanner mode')
        sleep(200)
        print('Button A=start nuker')
        sleep(200)
        print('Button B=stop nuker')
        start=+0
        
    
