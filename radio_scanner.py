from microbit import *
import radio
import microbit
scan_progress=print('scan in progress...')
message=radio.receive()
message_send='File "main.py", line 7, in <module>'
while True:
     for scanner in range(1,84):
         radio.config(channel=scanner)
         sleep(5)
         print('nothing',('found'),('in group'))
         if message is not None:
             print('recived message!')
             sleep(1000)
             print(message)
             sleep(2000)
             
