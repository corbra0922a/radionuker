from microbit import *
import radio
import microbit

    #I can't go to channel 99 the most I can do is 84 if I go over 84 I get this error:
    #ValueError: value out of range for argument 'channel'
    #I think it's because the microbit only has 84 channels
print('Initializing...')
sleep(2400)
print('Preparing...')
sleep(1500)
print('Applying finishing touches...')
sleep(2000)
print('3')
sleep(1000)
print('2')
sleep(1000)
print('1')
sleep(1000)
message='HI'
recieve=radio.receive()
while True:
    if recieve is not None:
        print('recived message!')
        print(recieve)
        sleep(5000)
    #1 through 84
    for i in range (1,84):
        #sets the radio channel to the value of i
        radio.config(channel=i)
        #sends the variable 'message'
        radio.send(message)
        #print 'group' and 'i' and also adds the word 'nuked' at the end
        print('channel',(i),('nuked'),('with'),('message'),(message))
        sleep(5)
