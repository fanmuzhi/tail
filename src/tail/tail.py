#  
import time
import sys,threading
import serial  
import binascii,encodings  
import re  
import socket  
from struct import * 

BAUDRATE =115200
PORT = 'COM4'
# 
mycom = serial.Serial(PORT, BAUDRATE)
if not mycom.isOpen():
    mycom.open()
line = mycom.readline()
while line:
    f = open('D:\COM_data\COM_DATA.txt','a')
    print(time.strftime("%Y-%m-%d %X\t") + line.strip())
    f.write(time.strftime("%Y-%m-%d %X\t") + line.strip() + '\n')  
    f.close( )
    line = mycom.readline()
mycom.close()

