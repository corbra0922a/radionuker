from microbit import *
import microbit
import radio
import math
import urandom

message=radio.receive()
radio_message=('.,-')
while True:
     for scanner in range(0,84):
         radio.config(channel=scanner)
         print('nothing',('found'),('in group'),(scanner))
         sleep(1)
         if message is not None:
             sleep(2000)
             print('recived message!')
             sleep(1000)
             print(message,('sent from channel',(scanner),))
             sleep(2200)
             radio.send(radio_message)
             print('sent message to channel',(scanner))
             sleep(1000)
             
