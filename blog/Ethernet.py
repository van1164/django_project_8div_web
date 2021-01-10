import socket 
from _thread import *
import time

tm = time.localtime(time.time())
tmday = time.strftime('[%Y-%m-%d]',tm)
timeString = time.strftime('[%Y-%m-%d %I:%M:%S %p]',tm)

Datafile = 0

Datafile = 0
line = []
packetData = []

# 쓰레드에서 실행되는 코드입니다. 

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다. 

def savelog(addr):    
    global packetData
    global tm
    LogFile = open('[' + str(addr[0]) + ']' + 'Log%s.log' % tmday,'a') 
    LogFile.write('\n')
    SourceData = ''.join(list(map(str,[' [Data Input by :', addr[0], ':', addr[1], ' ]'])))
    strPacket = list(map(str,packetData))
    LogFile.write(timeString)
    
    LogFile.write(SourceData)
    for i in strPacket :
        LogFile.write(i)
        LogFile.write(' ')
    LogFile.write('\n')
    LogFile.write('\n')
    LogFile.close()


def savePacket(addr):
    global packetData
    strPacket = list(map(str,packetData))
    Datafile = open( str(addr[0]) + ' Ethernet.ini','w')
    for c in strPacket :
        Datafile.write(c)
        Datafile.write(' ')
    Datafile.write('\n')
    Datafile.close()


def threaded(client_socket, addr): 
    global tm
    global tmday
    global timeString
    global line
    global packetData
    processNum = 0

    print('Connected by :', addr[0], ':', addr[1]) 



    # 클라이언트가 접속을 끊을 때 까지 반복합니다. 
    while True: 
        try:
            processNum+=1
            tm = time.localtime()
            tmday = time.strftime('[%Y-%m-%d]',tm)
            timeString = time.strftime('[%Y-%m-%d %I:%M:%S %p]',tm)

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            #
            if not data:
                break;
            client_socket.send(data) 
            for c in data :
                packetData.append(c)
                if c==0xf1 :
                    print('Data Input by :', addr[0], ':', addr[1])
                    print(packetData)
                    savePacket(addr)
                    savelog(addr)
                    del packetData[:]

            if processNum >= 120 : 
                print("Reset Socket")
                break
            
            

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 


HOST = '127.0.0.1'
PORT = 80

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", PORT)) 
server_socket.listen() 

print('server start')


# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다. 
while True: 

    print('wait')


    client_socket, addr = server_socket.accept() 
    start_new_thread(threaded, (client_socket, addr)) 

server_socket.close() 