import serial
import time
import signal
import threading
from . import views
from django.urls import path
from django.shortcuts import redirect
line = []
packetData = []
port = 'COM3'
baud = 115200

exitThread = False

def packetSave():
    global packetData
    global line
    
    for i in line:
        packetData.append(i)
            

def packetPrint():
    global packetData
    print(packetData)

def handler(signum,frame):
    exitThread = True
    

def parsing_data(data):
    print(data)
    
def readThread(ser):  
        global line
        global exitThread
        while not exitThread:
            for c in ser.read():
                line.append(c)
                #print(line)
                if c==0xA1:
                    packetSave()
                    packetPrint()
                    redirect('pre')
                    tmp = []
                    for i in packetData:
                        tmp.append(i)
                    del line[:]
                    del packetData[:]
                    return tmp
                    
        
        
"""   
if __name__ == "__main__":
    signal.signal(signal.SIGINT,handler)
    
    ser = serial.Serial(port,baud,timeout=0)
    
    thread = threading.Thread(target = readThread, args=(ser,))
    
    thread.start()
"""