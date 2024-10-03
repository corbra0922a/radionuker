from microbit import *
import microbit
import radio
import math
import urandom

scan_progress=print('scan in progress...')
message=radio.receive()
while True:
     for scanner in range(1,84):
         radio.config(channel=scanner)
         print('nothing',('found'),('in group'),(scanner))
         sleep(5)
         if message is not None:
             sleep(2000)
             print('recived message!')
             sleep(1000)
             print(message,('sent from channel',(scanner),))
             sleep(2000)
             
