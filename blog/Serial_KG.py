import serial
import signal
import threading
import time

tm = time.localtime(time.time())
tmday = time.strftime('[%Y-%m-%d]',tm)
timeString = time.strftime('[%Y-%m-%d %I:%M:%S %p]',tm)

Datafile = 0
line = []
packetData = []
port = 'COM4'
baud = 115200
exitThread = False
PlaceName = '';

def packetSave():
    global packetData
    global line
    
    for i in line:
        packetData.append(i);
        

def packetPrint():
    global packetData
    global timeString
    print(timeString, end='')
    print(' : ', end='')
    print(packetData)
    
def savePacket():
    global packetData
    strPacket = list(map(str,packetData))
    Datafile = open('%sSerial.ini' % PlaceName ,'w')   
    for i in strPacket :
        Datafile.write(i)
        Datafile.write(' ')
    Datafile.write('\n')
    Datafile.close()

def savelog():    
    global packetData
    global tm;
    LogFile = open('Log%s.log'%tmday,'a') 
    strPacket = list(map(str,packetData))
    LogFile.write(timeString)
    LogFile.write('  ')
    for i in strPacket :
        LogFile.write(i)
        LogFile.write(' ')
    LogFile.write('\n')
    LogFile.close();

def handler(signum,frame):
    exitThread = True
    

def parsing_data(data):
    print(data)
    
    
def readThread(ser):
    global tm
    global tmday
    global timeString
    global line
    global exitThread
    
    while not exitThread:
        tm = time.localtime()
        tmday = time.strftime('[%Y-%m-%d]',tm)
        timeString = time.strftime('[%Y-%m-%d %I:%M:%S %p]',tm)
        for c in ser.read():
            line.append(c)
            if c==0xF1:
                packetSave()
                packetPrint()
                savePacket();
                savelog();
                del line[:]
                del packetData[:]
    """     
    LogFile = open('Log%s.log'%tmday,'a')
    LogFile.write(timeString)
    LogFile.Write(' Connect End\n')
    """
    
                    
def FindSerial():
    ports = ['COM%s' % (i+1) for i in range(256)]
    
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except(OSError,serial.SerialException):
            pass
        
    return result

    
if __name__ == "__main__":
    
    print("접속 가능한 기기")
    print(FindSerial())
    
    while True:
        #print("접속할 포트 : ")
        PlaceName = input("차량이름 : ")
        
        port = input("접속할 포트 : ")
        port = port.upper()
        if port == 'EXIT':
            break;
        
        try :
            signal.signal(signal.SIGINT,handler)
            ser = serial.Serial(port,baud,timeout=0)
            thread = threading.Thread(target = readThread, args=(ser,))
            thread.start()
            break;
            
        except :
            print("접속 불가능한 포트입니다.")