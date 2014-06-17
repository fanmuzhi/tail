#-*- coding: utf-8 -*-
# import threading
import time
from time import sleep
from serial import Serial

class MySerial(object):
    def __init__(self):
#         threading.Thread.__init__(self)
        self.__terminate = False
        
    def open(self, settings):
        try:
            self.serial = Serial(settings["port"], settings["baudrate"], settings["bytesize"],
                    settings["parity"], settings["stopbits"], settings["timeout"])
            self.serial.flushInput()
            self.serial.flushOutput()
        except Exception, msg:
            return False, msg.message.decode("gbk")
        
        return True, "success"
            
    def terminate(self):
        self.__terminate = True
        
    def send(self, data, _type):
        self.serial.write(data)
    
    def __recv(self):
        data, quit = None, False
        while 1:
            if self.__terminate:
                break
            data = self.serial.read(1)
            if data == '':
                continue
            while 1:
                n = self.serial.inWaiting()
                if n > 0:
                    data = "%s%s" % (data, self.serial.read(n))
                    sleep(0.02) # data is this interval will be merged
                else:
                    quit = True
                    break
#                 data = "%s%s" % (data, self.serial.readline())
            if quit:
                break

        return data
    
    def catchByLine(self):
        line = self.serial.readline()
        if not line:
#             pass
            return None
        return line
    
    def close(self):
        if self.serial.isOpen():
            self.serial.close()
    
    def run(self):
        while 1:
            data = self.__recv()
#             data = self.catchByLine()
            if not data:
                break
            print (time.strftime("%Y-%m-%d %X\t") + data),

        self.serial.close()
        
if __name__ == "__main__":
    settings = {
                'port' : 3,
                'baudrate': 115200,
                'bytesize': 8,
                'parity': 'N',
                'stopbits': 1,
                'timeout': None
               }
    se = MySerial()
    se.open(settings)
    while 1:
        line = se.catchByLine()
        if line:
            print(time.strftime("%Y-%m-%d %X\t") + line.strip())
