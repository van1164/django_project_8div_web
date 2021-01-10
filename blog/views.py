from django.shortcuts import render
from .models import premier_league
from .models import news
import serial
import time
import signal
from . import urls
from django.shortcuts import redirect
from . import urls
import time
def what_time_is_it(nowtime, savetime):
    if(savetime==['']):
        return False
    if(int(savetime[0])>int(savetime[2])):
        if(nowtime[0]>=int(savetime[0]) and nowtime[0]<24):
            if(nowtime[0] == int(savetime[0]) and nowtime[1]<int(savetime[1])):
                return False
            else:
                return True
        elif(nowtime[0]>=0 and nowtime[0]<=int(savetime[2])):
            if(nowtime[0] == int(savetime[2]) and nowtime[1]>int(savetime[3])):
                return False
            else:
                return True                


    else:
        if(int(savetime[0])>nowtime[0]):
            return False
        elif(int(savetime[2])<nowtime[0]):
            return False
        elif(int(savetime[0]) == nowtime[0] and int(savetime[1])>nowtime[1]):
            return False
        elif(int(savetime[2]) == nowtime[0] and int(savetime[3])<nowtime[1]):
            return False
    return True
def this_time():
    time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
    return time_lst
def center(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)

    def what_time_is_it(nowtime, savetime):
        if(savetime==['']):
            return False
        if(int(savetime[0])>int(savetime[2])):
            if(nowtime[0]>=int(savetime[0]) and nowtime[0]<24):
                if(nowtime[0] == int(savetime[0]) and nowtime[1]<int(savetime[1])):
                    return False
                else:
                    return True
            elif(nowtime[0]>=0 and nowtime[0]<=int(savetime[2])):
                if(nowtime[0] == int(savetime[2]) and nowtime[1]>int(savetime[3])):
                    return False
                else:
                    return True                


        else:
            if(int(savetime[0])>nowtime[0]):
                return False
            elif(int(savetime[2])<nowtime[0]):
                return False
            elif(int(savetime[0]) == nowtime[0] and int(savetime[1])>nowtime[1]):
                return False
            elif(int(savetime[2]) == nowtime[0] and int(savetime[3])<nowtime[1]):
                return False
        return True

    yellow = 0
    red =0
    green = 0
    power = {}
    x = {}
    def this_time():
        time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
        return time_lst

    thistime = this_time()
    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)


    x['vr'] = int(result[8])
    x['Hum'] = int(result[10])
    #save static values
    invade =[]
    fire=[]
    password=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]


    for i in range(1,len(result),2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                firee = {}
                firee['alert']='발생'
                firee['color'] = 'background-color: red; font-weight: bold'
                fire.append(firee)
                red+=1
            else:
                firee = {}
                firee['alert']='양호'
                firee['color'] = 'background-color: #69eb78; font-weight: bold;'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                passs = {}
                passs['alert']='양호'
                passs['color'] = 'background-color: #69eb78; font-weight: bold;'
                password.append(passs)
                green+=1

            else:
                passs = {}
                passs['alert']='실종'
                passs['color'] = 'background-color: red; font-weight: bold'
                invade.password(passs)
                red+=1
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['ondo_color'] =  'background-color: blue; font-weight: bold'
                ondo.append(ondoo)
                red+=1
            elif(int(result[i+1])<=28):
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['ondo_color'] =  'background-color: #69eb78; font-weight: bold'
                ondo.append(ondoo)
                green+=1
            else:
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['ondo_color'] =  'background-color: red; font-weight: bold'
                ondo.append(ondoo)
                red+=1


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: red;'
                    door.append(doorr)
                    red +=1
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: rgb(255, 196, 34);'
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #69eb78;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = '경고'
                    windoow['color']='background-color: red; font-weight: bold'
                    window.append(windoow)  
                    red +=1
                else:
                    windoow = {}
                    windoow['alert'] = '열림'
                    windoow['color']='background-color: rgb(255, 196, 34); font-weight: bold'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = '닫힘'
                windoow['color']='background-color: #69eb78; font-weight: bold;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    lackk = {}
                    lackk['alert'] = '경고'
                    lackk['color']='background-color: red; font-weight: bold'
                    lack.append(lackk)
                    red +=1
                else:
                    lackk = {}
                    lackk['alert'] = '열림'
                    lackk['color']='background-color: rgb(255, 196, 34); font-weight: bold'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = '닫힘'
                lackk['color']='background-color: #69eb78; font-weight: bold;'
                lack.append(lackk)
                green +=1

    x['Door'] = door
    x['Fire'] = fire
    x['password'] = password
    x['invade'] = invade
    x['ondo'] = ondo

    #save save css of static values


    x['red']=red
    x['green'] = green
    x['yellow'] = yellow

    power['all'] = x

    r = open('blog/red.txt', 'r')
    p = r.read()
    if(p< str(red)):
        power['real'] = 1
    else:
        power['real'] = 0
    
    rdr = open('blog/red.txt', 'w')
    rdr.write(str(red))
    print(power)

    return render(request, 'blog/ArmySensor_call.html',power)


def mountain(request):
    return render(request, 'blog/mountain.html',{}) #splash html

def center_2(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)
    yellow = 0
    red =0
    green = 0
    power = {}
    x = {}
    password=[]
    thistime = this_time()
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-2,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : inline'
            password.append(passs)
            red+=1


    print(password)



    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)


    #save static values
    invade =[]
    fire=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]
    HM = []
    if(int(result[25])<=10):       #check ondo sensor
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#007bff'
        ondoo['ondo_color'] =  'fa fa-thermometer-quarter fa-7x'
        ondo.append(ondoo)
        red+=1
    elif(int(result[25])<=28):
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#5cb85c'
        ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
        ondo.append(ondoo)
        green+=1
    else:
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#a94442'
        ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
        ondo.append(ondoo)
        red+=1
    
    if(int(result[26])<=10):       #check HM sensor
        HMo = {}
        HMo['HM'] = result[26]
        HMo['color'] = '#007bff'
        HMo['HM_color'] =  'fa fa-thermometer-quarter fa-7x'
        HM.append(HMo)
        red+=1
    elif(int(result[26])<=28):
        HMo = {}
        HMo['HM'] = result[26]
        HMo['color'] = '#5cb85c'
        HMo['HM_color'] =  "fa fa-thermometer-half fa-7x"
        HM.append(HMo)
        green+=1
    else:
        HMo = {}
        HMo['HM'] = result[i+1]
        HMo['color'] = '#a94442'
        HMo['HM_color'] =  'fa fa-thermometer-full fa-7x'
        HM.append(HMo)
        red+=1

    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                firee = {}
                firee['alert']='fa fa-fire fa-7x'
                firee['color'] = '#5cb85c'
                firee['display'] = 'display:inline'
                fire.append(firee)
                red+=1

            else:
                firee = {}
                firee['alert']='fa fa-fire fa-7x'
                firee['color'] = '#5cb85c'
                firee['display'] = 'display:none'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'none'
                password.append(passs)
                green+=1


            else:
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'inline'
                password.append(passs)
                red+=1



        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: #a94442;'
                    door.append(doorr)
                    red +=1
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: #ffc107; '
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #5cb85c;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-restore fa-5x'
                    windoow['color']='color: #a94442;'
                    window.append(windoow)  
                    red +=1
                else:
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-store fa-5x'
                    windoow['color']='color: #ffc107;'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = 'fa fa-map fa-5x'
                windoow['color']='color: #5cb85c;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color: #a94442'
                    lack.append(lackk)
                    red +=1
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1

    x['Door'] = door
    x['Fire'] = fire
    x['password'] = password
    x['invade'] = invade
    x['ondo'] = ondo
    x['window'] = window
    #save save css of static values
    x['lack'] =lack
    x['HM'] =HM
    x['red']=red
    x['green'] = green
    x['yellow'] = yellow

    power['all'] = x

    r = open('blog/red.txt', 'r')
    p = r.read()
    if(p==""):
        p = "0"
    if(int(p)< int(red)):
        power['real'] = 1
    else:
        power['real'] = 0
    
    rdr = open('blog/red.txt', 'w')
    rdr.write(str(red))
    print(power)
    return render(request, 'blog/ArmySensor_call2.html',power)

def center_3(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)


    yellow = 0
    red =0
    green = 0
    power = {}
    x = {}
    password=[]
    thistime = this_time()
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-3,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : inline'
            password.append(passs)
            red+=1


    print(password)



    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)



    

    x['vr'] = int(result[8])
    x['Hum'] = int(result[10])
    #save static values
    invade =[]
    fire=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]


    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                firee = {}
                firee['alert']='발생'
                firee['color'] = 'background-color: red; font-weight: bold'
                fire.append(firee)
                red+=1
            else:
                firee = {}
                firee['alert']='양호'
                firee['color'] = 'background-color: #69eb78; font-weight: bold;'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['dispay'] = 'none'
                password.append(passs)
                green+=1

            else:
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'inline'
                password.append(passs)
                red+=1
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#007bff'
                ondoo['ondo_color'] =  'fa fa-thermometer-quarter fa-7x'
                ondo.append(ondoo)
                red+=1
            elif(int(result[i+1])<=28):
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#5cb85c'
                ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
                ondo.append(ondoo)
                green+=1
            else:
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#a94442'
                ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
                ondo.append(ondoo)
                red+=1


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: #a94442;'
                    door.append(doorr)
                    red +=1
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: #ffc107; '
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #69eb78;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-restore fa-5x'
                    windoow['color']='color: #a94442;'
                    window.append(windoow)  
                    red +=1
                else:
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-store fa-5x'
                    windoow['color']='color: #ffc107;'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = 'fa fa-map fa-5x'
                windoow['color']='color: #5cb85c;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color: #a94442'
                    lack.append(lackk)
                    red +=1
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1

    x['Door'] = door
    x['Fire'] = fire
    x['password'] = password
    x['invade'] = invade
    x['ondo'] = ondo
    x['window'] = window
    #save save css of static values
    x['lack'] =lack

    x['red']=red
    x['green'] = green
    x['yellow'] = yellow

    power['all'] = x

    r = open('blog/red.txt', 'r')
    p = r.read()
    if(p< str(red)):
        power['real'] = 1
    else:
        power['real'] = 0
    
    rdr = open('blog/red.txt', 'w')
    rdr.write(str(red))
    print(power)
    return render(request, 'blog/ArmySensor_call3.html',power)

def center_4(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)

    def what_time_is_it(nowtime, savetime):
        if(savetime==['']):
            return False
        if(int(savetime[0])>int(savetime[2])):
            if(nowtime[0]>=int(savetime[0]) and nowtime[0]<24):
                if(nowtime[0] == int(savetime[0]) and nowtime[1]<int(savetime[1])):
                    return False
                else:
                    return True
            elif(nowtime[0]>=0 and nowtime[0]<=int(savetime[2])):
                if(nowtime[0] == int(savetime[2]) and nowtime[1]>int(savetime[3])):
                    return False
                else:
                    return True                


        else:
            if(int(savetime[0])>nowtime[0]):
                return False
            elif(int(savetime[2])<nowtime[0]):
                return False
            elif(int(savetime[0]) == nowtime[0] and int(savetime[1])>nowtime[1]):
                return False
            elif(int(savetime[2]) == nowtime[0] and int(savetime[3])<nowtime[1]):
                return False
        return True

    yellow = 0
    red =0
    green = 0
    power = {}
    x = {}
    def this_time():
        time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
        return time_lst
    password=[]
    thistime = this_time()
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-3,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : inline'
            password.append(passs)
            red+=1


    print(password)



    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)



    

    x['vr'] = int(result[8])
    x['Hum'] = int(result[10])
    #save static values
    invade =[]
    fire=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]


    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                firee = {}
                firee['alert']='발생'
                firee['color'] = 'background-color: red; font-weight: bold'
                fire.append(firee)
                red+=1
            else:
                firee = {}
                firee['alert']='양호'
                firee['color'] = 'background-color: #69eb78; font-weight: bold;'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['dispay'] = 'none'
                password.append(passs)
                green+=1

            else:
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'inline'
                password.append(passs)
                red+=1
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#007bff'
                ondoo['ondo_color'] =  'fa fa-thermometer-quarter fa-7x'
                ondo.append(ondoo)
                red+=1
            elif(int(result[i+1])<=28):
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#5cb85c'
                ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
                ondo.append(ondoo)
                green+=1
            else:
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#a94442'
                ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
                ondo.append(ondoo)
                red+=1


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: #a94442;'
                    door.append(doorr)
                    red +=1
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: #ffc107; '
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #69eb78;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-restore fa-5x'
                    windoow['color']='color: #a94442;'
                    window.append(windoow)  
                    red +=1
                else:
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-store fa-5x'
                    windoow['color']='color: #ffc107;'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = 'fa fa-map fa-5x'
                windoow['color']='color: #5cb85c;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==0):
                if(what_time_is_it(thistime, tmlst)):
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color: #a94442'
                    lack.append(lackk)
                    red +=1
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1

    x['Door'] = door
    x['Fire'] = fire
    x['password'] = password
    x['invade'] = invade
    x['ondo'] = ondo
    x['window'] = window
    #save save css of static values
    x['lack'] =lack

    x['red']=red
    x['green'] = green
    x['yellow'] = yellow

    power['all'] = x

    r = open('blog/red.txt', 'r')
    p = r.read()
    if(p< str(red)):
        power['real'] = 1
    else:
        power['real'] = 0
    
    rdr = open('blog/red.txt', 'w')
    rdr.write(str(red))
    print(power)
    return render(request, 'blog/ArmySensor_call4.html',power)


def popup(request):
    
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)

    def what_time_is_it(nowtime, savetime):
        if(savetime==['']):
            return False
        if(int(savetime[0])>int(savetime[2])):
            if(nowtime[0]>=int(savetime[0]) and nowtime[0]<24):
                if(nowtime[0] == int(savetime[0]) and nowtime[1]<int(savetime[1])):
                    return False
                else:
                    return True
            elif(nowtime[0]>=0 and nowtime[0]<=int(savetime[2])):
                if(nowtime[0] == int(savetime[2]) and nowtime[1]>int(savetime[3])):
                    return False
                else:
                    return True                


        else:
            if(int(savetime[0])>nowtime[0]):
                return False
            elif(int(savetime[2])<nowtime[0]):
                return False
            elif(int(savetime[0]) == nowtime[0] and int(savetime[1])>nowtime[1]):
                return False
            elif(int(savetime[2]) == nowtime[0] and int(savetime[3])<nowtime[1]):
                return False
        return True

    yellow = 0
    red =[]
    green = 0
    power = {}
    x = {}
    def this_time():
        time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
        return time_lst
    password=[]
    thistime = this_time()
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-3,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            red.append("암호장비 사라짐")


    print(password)



    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)



    

    x['vr'] = int(result[8])
    x['Hum'] = int(result[10])
    #save static values
    invade =[]
    fire=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]


    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                red.append("정보통신대대 화재 발생")
            else:
                firee = {}
                firee['alert']='양호'
                firee['color'] = 'background-color: #69eb78; font-weight: bold;'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                red.append("암호모듈 사라짐")

            else:
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'inline'
                password.append(passs)
                red+=1
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                red.append("기온 하락")
                ondo.append(ondoo)
                red+=1
            elif(int(result[i+1])<=28):
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#5cb85c'
                ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
                ondo.append(ondoo)
                green+=1
            else:
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#a94442'
                ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
                ondo.append(ondoo)
                red+=1


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: #a94442;'
                    door.append(doorr)
                    red.append("출입문 열림")
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: #ffc107; '
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #69eb78;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-restore fa-5x'
                    windoow['color']='color: #a94442;'
                    window.append(windoow)  
                    red.append("정보통신센터 창문열림")
                else:
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-store fa-5x'
                    windoow['color']='color: #ffc107;'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = 'fa fa-map fa-5x'
                windoow['color']='color: #5cb85c;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red.append("정보통신센터 랙장비 문열림")
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1


    all = {'red':red}




    return render(request, 'blog/popup.html', all)


def timeset(request):
    dictt = {}
    rdr = open('blog/timeset.txt','r')
    pp = rdr. read()
    result = pp.split(" ")
    dictt['start1'] = result[0]
    dictt['start2'] = result[2]
    dictt['end1'] = result[1]
    dictt['end2'] = result[3]
    return render(request, 'blog/timeset.html',dictt)
def saved(request):
    if request.method == "POST":
        start1 = request.POST.get("starttime1", None)
        end1 = request.POST.get("endtime1", None)
        start2 = request.POST.get("starttime2", None)
        end2 = request.POST.get("endtime2", None)
        rdr = open('blog/timeset.txt', 'w')
        rdr.write(start1)
        rdr.write(" ")
        rdr.write(start2)
        rdr.write(" ")
        rdr.write(end1)
        rdr.write(" ")
        rdr.write(end2)
        rdr.close()
    return render(request, 'blog/finish.html',{})

def Login(request):
    x = {'id':"", 'pw':""}
    x = {'lst':x}
    return render(request, 'blog/Login.html',x) #splash html

def detect(request):
    print(request.method)
    # if request.method == "POST":
    #     uid = request.POST.get("username", None)
    #     pw = request.POST.get("password", None)
    #     if(uid == "admin" and pw == "admin"):
    return restart(request)
    #     else:
    #         return redirect("http://192.168.1.101:8080/Login_re")
    # return redirect("http://192.168.1.101:8080/")

def Login_re(request):
    return render(request, 'blog/Login_re.html',{}) #splash html


def Home(request):
    def this_time():
        time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
        return time_lst

    thistime = this_time()

    if request.method == "POST":
        uid = request.POST.get("username", None)
        pw = request.POST.get("password", None)
        cycle =True
        if(uid == "admin" and pw == "admin"):
            """ ----------------------id = 66---------------------------"""
            green = 0
            yellow = 0
            red =0
            power = {}
            x = {}

            tx = open('blog/atcis66Serial.ini','r')
            tmp = tx.read()             #read database
            print(tmp)                  #print database 
            result = tmp.split(" ")     #save database to list(result)
            print(result)               #print list(result)

            x['vr'] = int(result[8])
            x['ondo'] = int(result[9])
            x['Hum'] = int(result[10])
            #save static values

            for i in range(1,15,2):
                if(int(result[i])==4):              #check invader sensor 
                    if(int(result[i+1])<=70):
                        x['invade'] = '출현'
                        x['invade_color'] = 'background-color: red; font-weight: bold'
                        red+=1
                    else:
                        x['invade'] = '없음'
                        x['invade_color'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1
                if(int(result[i])==2):              #check Fire sensor 
                    if(int(result[i+1])==1):
                        x['Fire'] = '발생'
                        x['Fire_color'] = 'background-color: red; font-weight: bold'
                        red+=1
                    else:
                        x['Fire'] = '양호'
                        x['Fire_color'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1

                if(int(result[i])==3):              #check password module 
                    if(int(result[i+1])<15):
                        x['password'] = '양호'
                        x['password_color'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1

                    else:
                        x['password'] = '실종'
                        x['password_color'] = 'background-color: red; font-weight: bold'
                        red+=1
                        


                if(int(result[i])==1):              #check Door sensor 
                    if(int(result[i+1])==1):
                        if(what_time_is_it(thistime, tmlst)):
                            x['Door'] = '경고'
                            x['Door_color'] = 'background-color: red; font-weight: bold'
                            red +=1
                        else:
                            x['Door'] = '열림'
                            x['Door_color'] = 'background-color: rgb(255, 196, 34); font-weight: bold'
                            yellow +=1
                    else:
                        x['Door'] = '닫힘'
                        x['Door_color'] = 'background-color: #69eb78; font-weight: bold;'
                        green +=1



            if(int(result[10])>=20):        #check HM sensor
                x['vr_color'] =  'background-color: red; font-weight: bold'
            else:
                x['vr_color'] =  'background-color: #69eb78; color:white; font-weight: bold'
            


            if(int(result[9])<=10):       #check ondo sensor
                x['ondo_color'] =  'background-color: blue; font-weight: bold'
                red+=1
            elif(int(result[9])<=28):
                x['ondo_color'] =  'background-color: #69eb78; font-weight: bold'
                green+=1
            else:
                x['ondo_color'] =  'background-color: red; font-weight: bold'
                red+=1
            green_67 = 0
            yellow_67 = 0
            red_67 =0

            y = {}
            tx = open('blog/atcis67Serial.ini','r')
            tmp67 = tx.read()             #read database
            print(tmp67)                  #print database 
            result67 = tmp67.split(" ")     #save database to list(result)
            print(result67)               #print list(result)


            y['vr67'] = int(result67[8])
            y['ondo67'] = int(result67[9])
            y['Hum67'] = int(result67[10])
            #save static values

            for i in range(1,15,2):
                if(int(result67[i])==4):              #check invader sensor 
                    if(int(result67[i+1])<=70):
                        y['invade67'] = '출현'
                        y['invade_color67'] = 'background-color: red; font-weight: bold'
                        red+=1
                    else:
                        y['invade67'] = '없음'
                        y['invade_color67'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1
                if(int(result67[i])==2):              #check Fire sensor 
                    if(int(result67[i+1])==1):
                        y['Fire67'] = '발생'
                        y['Fire_color67'] = 'background-color: red; font-weight: bold'
                        red+=1
                    else:
                        y['Fire67'] = '양호'
                        y['Fire_color67'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1

                if(int(result67[i])==3):              #check password module 
                    if(int(result67[i+1])<15):
                        y['password67'] = '양호'
                        y['password_color67'] = 'background-color: #69eb78; font-weight: bold;'
                        green+=1

                    else:
                        y['password67'] = '실종'
                        y['password_color67'] = 'background-color: red; font-weight: bold'
                        red+=1
                        


                if(int(result67[i])==1):              #check Door sensor 
                    if(int(result67[i+1])==1):
                        if(what_time_is_it(thistime, tmlst)):
                            y['Door67'] = '경고'
                            y['Door_color67'] = 'background-color: red; font-weight: bold'
                            red +=1
                        else:
                            y['Door67'] = '열림'
                            y['Door_color67'] = 'background-color: rgb(255, 196, 34); font-weight: bold'
                            yellow +=1
                    else:
                        y['Door67'] = '닫힘'
                        y['Door_color67'] = 'background-color: #69eb78; font-weight: bold;'
                        green +=1



            if(int(result67[10])>=20):        #check HM sensor
                y['vr_color67'] =  'background-color: red; font-weight: bold'
            else:
                y['vr_color67'] =  'background-color: #69eb78; color:white; font-weight: bold'
            


            if(int(result67[9])<=10):       #check ondo sensor
                y['ondo_color67'] =  'background-color: blue; font-weight: bold'
                red+=1
            elif(int(result67[9])<=28):
                y['ondo_color67'] =  'background-color: #69eb78; font-weight: bold'
                green+=1
            else:
                y['ondo_color67'] =  'background-color: red; font-weight: bold'
                red+=1


            #save save css of static values




            x['red']=red +red_67
            x['green'] = green + green_67
            x['yellow'] = yellow + yellow_67

            power['all'] = x



            power['all67'] = y
            r = open('blog/red.txt', 'r')
            p = r.read()
            if(p< str(red+red_67)):
                power['real'] = 1
            else:
                power['real'] = 0
            
            rdr = open('blog/red.txt', 'w')
            rdr.write(str(red + red_67))


            return render(request, 'blog/ArmySensor.html',power) #splash html


        else:
            return redirect("http://192.168.1.101:8080/")
    return redirect("http://192.168.1.101:8080/")
 




#green.html view
def green(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")


    green = []
    power = {}
    x = {}


    thistime = this_time()
    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)

    for i in range(1,len(result),2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                pass
            else:
                green.append("정보통신센터 거수자없음")
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                pass
            else:
                green.append("정보통신센터 화재없음")

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                green.append("정보통신센터 암호모듈 정상")

            else:
                pass
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                pass
            elif(int(result[i+1])<=28):
                green.append("정보통신센터 온도 정상")
            else:
                pass


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    pass
            else:          
                green.append("정보통신센터 문 정상")
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    pass
            else:
                green.append("정보통신센터 창문 정상")

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    pass
            else:
                green.append("정보통신센터 랙장비 정상")


    power['all'] = green
    return render(request, 'blog/green.html',power)



#yellow.html view
def yellow(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")

    yellow = []
    thistime = this_time()

    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)


    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                pass
            else:
                pass
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                pass
            else:
                pass

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                pass
            else:
                pass

        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                pass
            elif(int(result[i+1])<=28):
                pass
            else:
                pass


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    yellow.append("문 열림")
            else:
                pass
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    yellow.append("창문 열림")
            else:
                pass

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    pass
                else:
                    yellow.append("랙 장비 문열림")
            else:
                pass

    alll = {}
    alll['yellow'] = yellow
    return render(request, 'blog/yellow.html',alll)



#red.html view
def red(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)

    def what_time_is_it(nowtime, savetime):
        if(savetime==['']):
            return False
        if(int(savetime[0])>int(savetime[2])):
            if(nowtime[0]>=int(savetime[0]) and nowtime[0]<24):
                if(nowtime[0] == int(savetime[0]) and nowtime[1]<int(savetime[1])):
                    return False
                else:
                    return True
            elif(nowtime[0]>=0 and nowtime[0]<=int(savetime[2])):
                if(nowtime[0] == int(savetime[2]) and nowtime[1]>int(savetime[3])):
                    return False
                else:
                    return True                


        else:
            if(int(savetime[0])>nowtime[0]):
                return False
            elif(int(savetime[2])<nowtime[0]):
                return False
            elif(int(savetime[0]) == nowtime[0] and int(savetime[1])>nowtime[1]):
                return False
            elif(int(savetime[2]) == nowtime[0] and int(savetime[3])<nowtime[1]):
                return False
        return True

    yellow = 0
    red =[]
    green = 0
    power = {}
    x = {}
    def this_time():
        time_lst = [time.localtime().tm_hour, time.localtime().tm_min]
        return time_lst
    password=[]
    thistime = this_time()
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-3,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            red.append("암호장비 사라짐")


    print(password)



    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)



    

    x['vr'] = int(result[8])
    x['Hum'] = int(result[10])
    #save static values
    invade =[]
    fire=[]
    door=[]
    ondo=[]
    window = []
    lack = []
    suwe=[]


    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                red.append("정보통신센터 거수자 출현")
            else:
                pass
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                red.append("정보통신센터 화재발생")
            else:
                pass

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                red.append("암호모듈 사라짐")
            else:
                pass
        if(int(result[i])==8):
            if(int(result[i+1])<=10):       #check ondo sensor
                red.append("기온 하락")
                ondo.append(ondoo)
                red+=1
            elif(int(result[i+1])<=28):
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#5cb85c'
                ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
                ondo.append(ondoo)
                green+=1
            else:
                ondoo = {}
                ondoo['ondo'] = result[i+1]
                ondoo['color'] = '#a94442'
                ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
                ondo.append(ondoo)
                red+=1


        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red.append("정보통신센터 문열림")
                else:
                    pass
            else:
                pass
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red.append("정보통신센터 창문열림")
                else:
                    pass
            else:
                pass

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red.append("정보통신센터 랙장비 문열림")
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1


    all = {'red':red}




    return render(request, 'blog/red.html',all)










def restart(request):
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")
    print(tmlst)


    yellow = 0
    red =0
    green = 0
    power = {}
    x = {}
    password = []
    tx = open('blog/192.168.1.150 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)
    for i in range(2,len(result)-3,2):
        if(int(result[i])<15):
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : none'
            password.append(passs)
            green+=1

        else:
            passs = {}
            passs['alert']='fa fa-digital-tachograph fa-stack-1x'
            passs['color'] = '#5cb85c'
            passs['display'] = 'display : inline'
            password.append(passs)
            red+=1


    thistime = this_time()
    tx = open('blog/192.168.1.170 Ethernet.ini','r')
    tmp = tx.read()             #read database
    print(tmp)                  #print database 
    result = tmp.split(" ")     #save database to list(result)
    print(result)               #print list(result)

    ondo=[]
    HM = []
    door = []
    window = []
    lack = []
    HM = []
    fire = []
    invade = []
    

    if(int(result[25])<=10):       #check ondo sensor
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#007bff'
        ondoo['ondo_color'] =  'fa fa-thermometer-quarter fa-7x'
        ondo.append(ondoo)
        red+=1
    elif(int(result[25])<=28):
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#5cb85c'
        ondoo['ondo_color'] =  "fa fa-thermometer-half fa-7x"
        ondo.append(ondoo)
        green+=1
    else:
        ondoo = {}
        ondoo['ondo'] = result[25]
        ondoo['color'] = '#a94442'
        ondoo['ondo_color'] =  'fa fa-thermometer-full fa-7x'
        ondo.append(ondoo)
        red+=1
    
    if(int(result[26])<=10):       #check HM sensor
        HMo = {}
        HMo['HM'] = result[26]
        HMo['color'] = '#007bff'
        HMo['HM_color'] =  'fa fa-thermometer-quarter fa-7x'
        HM.append(HMo)
        red+=1
    elif(int(result[26])<=28):
        HMo = {}
        HMo['HM'] = result[26]
        HMo['color'] = '#5cb85c'
        HMo['HM_color'] =  "fa fa-thermometer-half fa-7x"
        HM.append(HMo)
        green+=1
    else:
        HMo = {}
        HMo['HM'] = result[i+1]
        HMo['color'] = '#a94442'
        HMo['HM_color'] =  'fa fa-thermometer-full fa-7x'
        HM.append(HMo)
        red+=1

    for i in range(1,len(result)-1,2):
        if(int(result[i])==6):              #check invader sensor 
            if(int(result[i+1])<=70):
                invadee = {}
                invadee['alert']='출현'
                invadee['color'] = 'background-color: red; font-weight: bold'
                invade.append(invadee)
                red+=1
            else:
                invadee = {}
                invadee['alert']='없음'
                invadee['color'] = 'background-color: #69eb78; font-weight: bold;'
                invade.append(invadee)
                green+=1
        if(int(result[i])==4):              #check Fire sensor 
            if(int(result[i+1])==1):
                firee = {}
                firee['alert']='발생'
                firee['color'] = 'background-color: red; font-weight: bold'
                fire.append(firee)
                red+=1
            else:
                firee = {}
                firee['alert']='양호'
                firee['color'] = 'background-color: #69eb78; font-weight: bold;'
                fire.append(firee)
                green+=1

        if(int(result[i])==5):              #check password module 
            if(int(result[i+1])<15):
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['dispay'] = 'none'
                password.append(passs)
                green+=1

            else:
                passs = {}
                passs['alert']='fa fa-digital-tachograph fa-stack-1x'
                passs['color'] = '#5cb85c'
                passs['display'] = 'inline'
                password.append(passs)
                red+=1



        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    doorr = {}
                    doorr['alert']='fa fa-door-open fa-5x'
                    doorr['color'] = 'color: #a94442;'
                    door.append(doorr)
                    red +=1
                else:
                    doorr = {}
                    doorr['alert'] = 'fa fa-door-open fa-5x'
                    doorr['color']='color: #ffc107; '
                    door.append(doorr)
                    yellow +=1
            else:
                doorr = {}
                doorr['alert'] = 'fa fa-door-closed fa-5x'
                doorr['color']='color: #69eb78;'
                door.append(doorr)                
                green +=1
        
        if(int(result[i])==2):              #check Window sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-restore fa-5x'
                    windoow['color']='color: #a94442;'
                    window.append(windoow)  
                    red +=1
                else:
                    windoow = {}
                    windoow['alert'] = 'fa fa-window-store fa-5x'
                    windoow['color']='color: #ffc107;'
                    window.append(windoow)
                    yellow +=1
            else:
                windoow = {}
                windoow['alert'] = 'fa fa-map fa-5x'
                windoow['color']='color: #5cb85c;'
                window.append(windoow)
                green +=1

        if(int(result[i])==3):              #check Lack sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color: #a94442'
                    lack.append(lackk)
                    red +=1
                else:
                    lackk = {}
                    lackk['alert'] = 'fa fa-door-open fa-5x'
                    lackk['color']='color:#ffc107'
                    lack.append(lackk)
                    yellow +=1
            else:
                lackk = {}
                lackk['alert'] = 'fa fa-door-closed fa-5x'
                lackk['color']='color: #5cb85c'
                lack.append(lackk)
                green +=1

    x['Door'] = door
    x['Fire'] = fire
    x['password'] = password
    x['invade'] = invade
    x['ondo'] = ondo
    x['window'] = window
    #save save css of static values
    x['lack'] =lack
    x['HM'] =HM
    x['red']=red
    x['green'] = green
    x['yellow'] = yellow



    if(red>=1):
        x['xxxx'] = "fa fx-smile fa-7x"
    else:
        x['xxxx'] = "fa fa-smile fa-7x"
    power['all'] = x


    r = open('blog/red.txt', 'r')
    p = r.read()
    print(red)
    print(p)
    if(int(p)< int(red)):
        power['real'] = 1
    else:
        power['real'] = 0
    
    rdr = open('blog/red.txt', 'w')
    rdr.write(str(red))

    return render(request, 'blog/ArmySensor.html',power) #splash html










def league_stats(request):
    return render(request, 'blog/league_stats.html',{})
    