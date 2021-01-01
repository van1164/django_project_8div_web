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
                red_67+=1
            else:
                y['invade67'] = '없음'
                y['invade_color67'] = 'background-color: #69eb78; font-weight: bold;'
                green_67+=1
        if(int(result67[i])==2):              #check Fire sensor 
            if(int(result67[i+1])==1):
                y['Fire67'] = '발생'
                y['Fire_color67'] = 'background-color: red; font-weight: bold'
                red_67+=1
            else:
                y['Fire67'] = '양호'
                y['Fire_color67'] = 'background-color: #69eb78; font-weight: bold;'
                green_67+=1

        if(int(result67[i])==3):              #check password module 
            if(int(result67[i+1])<15):
                y['password67'] = '양호'
                y['password_color67'] = 'background-color: #69eb78; font-weight: bold;'
                green_67+=1

            else:
                y['password67'] = '실종'
                y['password_color67'] = 'background-color: red; font-weight: bold'
                red_67+=1
                


        if(int(result67[i])==1):              #check Door sensor 
            if(int(result67[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    y['Door67'] = '경고'
                    y['Door_color67'] = 'background-color: red; font-weight: bold'
                    red_67 +=1
                else:
                    y['Door67'] = '열림'
                    y['Door_color67'] = 'background-color: rgb(255, 196, 34); font-weight: bold'
                    yellow_67 +=1
            else:
                y['Door67'] = '닫힘'
                y['Door_color67'] = 'background-color: #69eb78; font-weight: bold;'
                green_67 +=1



    if(int(result67[10])>=20):        #check HM sensor
        y['vr_color67'] =  'background-color: red; font-weight: bold'
    else:
        y['vr_color67'] =  'background-color: #69eb78; color:white; font-weight: bold'
    


    if(int(result67[9])<=10):       #check ondo sensor
        y['ondo_color67'] =  'background-color: blue; font-weight: bold'
        red_67+=1
    elif(int(result67[9])<=28):
        y['ondo_color67'] =  'background-color: #69eb78; font-weight: bold'
        green_67+=1
    else:
        y['ondo_color67'] =  'background-color: red; font-weight: bold'
        red_67+=1


    #save save css of static values




    x['red']=red
    x['green'] = green
    x['yellow'] = yellow

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





    return render(request, 'blog/ArmySensor_call.html',power)


# 장고 모듈
def popupMid(request):
    return render(request, 'blog/popupmiddle.html',{})


def popup(request):
    
    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")


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

    thistime = this_time()


    red_list = []
    """--------------------------------66-----------------------------------------"""
    tx = open('blog/atcis66Serial.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)
    for i in range(1,15,2):
        if(int(result[i])==4):              #check invader sensor 
            if(int(result[i+1])<=70):
                red_list.append("66 쉘터차량 거수자 출현")
        if(int(result[i])==2):              #check Fire sensor 
            if(int(result[i+1])==1):
                red_list.append("66 쉘터차량 화재발생")
        if(int(result[i])==3):              #check password module 
            if(int(result[i+1])>=15):
                red_list.append("66 쉘터차량 암호모듈 실종")
        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red_list.append("66 쉘터차량 문열림")


    if(int(result[9])<=10):       #check ondo sensor
        red_list.append("66 쉘터차량 온도 낮음")
    elif(int(result[9])>28):
        red_list.append("66 쉘터차량 온도 높음")


        

    """--------------------------------67-----------------------------------------"""


    txx = open('blog/atcis67Serial.ini','r')
    tmpp = txx.read()             #read database
    result_67 = tmpp.split(" ")     #save database to list(result_67)
    for i in range(1,15,2):
        if(int(result_67[i])==4):              #check invader sensor 
            if(int(result_67[i+1])<=70):
                red_list.append("67 쉘터차량 거수자 출현")
        if(int(result_67[i])==2):              #check Fire sensor 
            if(int(result_67[i+1])==1):
                red_list.append("67 쉘터차량 화재발생")
        if(int(result_67[i])==3):              #check password module 
            if(int(result_67[i+1])>=15):
                red_list.append("67 쉘터차량 암호모듈 실종")
        if(int(result_67[i])==1):              #check Door sensor 
            if(int(result_67[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red_list.append("67 쉘터차량 문열림")


    if(int(result_67[9])<=10):       #check ondo sensor
        red_list.append("67 쉘터차량 온도 낮음")
    elif(int(result_67[9])>28):
        red_list.append("67 쉘터차량 온도 높음")

    all = {'red':red_list}




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
    if request.method == "POST":
        uid = request.POST.get("username", None)
        pw = request.POST.get("password", None)
        if(uid == "admin" and pw == "admin"):
            return Home(request)
        else:
            return redirect("http://192.168.1.101:8080/Login_re")
    return redirect("http://192.168.1.101:8080/")

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
    """--------------------------------66-----------------------------------------"""
    tx = open('blog/atcis66Serial.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)
    green_list = []

    for i in range(1,15,2):
        if(int(result[i])==4):              #check invader sensor 
            if(int(result[i+1])>70):
                green_list.append("66 쉘터차량 거수자 없음")
        if(int(result[i])==2):              #check Fire sensor 
            if(int(result[i+1])!=1):
                green_list.append("66 쉘터차량 화재 없음")

        if(int(result[i])==3):              #check password module 
            if(int(result[i+1])<15):
                green_list.append("66 쉘터차량 암호모듈 양호")
        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])!=1):
                green_list.append("66 쉘터차량 문닫힘")

    if(int(result[9])<=28 and int(result[9])>10):
        green_list.append("66 쉘터차량 온도 정상")

    """-----------------------------------67-----------------------------------------"""

    ttx = open('blog/atcis67Serial.ini','r')
    tmpp = ttx.read()             #read database
    result_67 = tmpp.split(" ")     #save database to list(result)

    for i in range(1,15,2):
        if(int(result_67[i])==4):              #check invader sensor 
            if(int(result_67[i+1])>70):
                green_list.append("67 쉘터차량 거수자 없음")
        if(int(result_67[i])==2):              #check Fire sensor 
            if(int(result_67[i+1])!=1):
                green_list.append("67 쉘터차량 화재 없음")

        if(int(result_67[i])==3):              #check password module 
            if(int(result_67[i+1])<15):
                green_list.append("67 쉘터차량 암호모듈 양호")
        if(int(result_67[i])==1):              #check Door sensor 
            if(int(result_67[i+1])!=1):
                green_list.append("67 쉘터차량 문닫힘")

    if(int(result_67[9])<=28 and int(result_67[9])>10):
        green_list.append("67 쉘터차량 온도 정상")
    all = {'green':green_list}
    return render(request, 'blog/green.html',all)



#yellow.html view
def yellow(request):
    yellow_list = []
    """--------------------------------66-----------------------------------------"""
    tx = open('blog/atcis66Serial.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)
    for i in range(1,15,2):
        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                yellow_list.append("66 쉘터차량 문열림")
    """--------------------------------67-----------------------------------------"""


    txx = open('blog/atcis67Serial.ini','r')
    tmpp = txx.read()             #read database
    result_67 = tmpp.split(" ")     #save database to list(result_67)
    for i in range(1,15,2):
        if(int(result_67[i])==1):              #check Door sensor 
            if(int(result_67[i+1])==1):
                yellow_list.append("67쉘터차량 문열림")

    all = {'yellow':yellow_list}
    return render(request, 'blog/yellow.html',all)



#red.html view
def red(request):

    opn = open('blog/timeset.txt','r')
    op = opn.read()
    tmlst = op.split(" ")


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

    thistime = this_time()


    red_list = []
    """--------------------------------66-----------------------------------------"""
    tx = open('blog/atcis66Serial.ini','r')
    tmp = tx.read()             #read database
    result = tmp.split(" ")     #save database to list(result)
    for i in range(1,15,2):
        if(int(result[i])==4):              #check invader sensor 
            if(int(result[i+1])<=70):
                red_list.append("66 쉘터차량 거수자 출현")
        if(int(result[i])==2):              #check Fire sensor 
            if(int(result[i+1])==1):
                red_list.append("66 쉘터차량 화재발생")
        if(int(result[i])==3):              #check password module 
            if(int(result[i+1])>=15):
                red_list.append("66 쉘터차량 암호모듈 실종")
        if(int(result[i])==1):              #check Door sensor 
            if(int(result[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red_list.append("66 쉘터차량 문열림")


    if(int(result[9])<=10):       #check ondo sensor
        red_list.append("66 쉘터차량 온도 낮음")
    elif(int(result[9])>28):
        red_list.append("66 쉘터차량 온도 높음")


        

    """--------------------------------67-----------------------------------------"""


    txx = open('blog/atcis67Serial.ini','r')
    tmpp = txx.read()             #read database
    result_67 = tmpp.split(" ")     #save database to list(result_67)
    for i in range(1,15,2):
        if(int(result_67[i])==4):              #check invader sensor 
            if(int(result_67[i+1])<=70):
                red_list.append("67 쉘터차량 거수자 출현")
        if(int(result_67[i])==2):              #check Fire sensor 
            if(int(result_67[i+1])==1):
                red_list.append("67 쉘터차량 화재발생")
        if(int(result_67[i])==3):              #check password module 
            if(int(result_67[i+1])>=15):
                red_list.append("67 쉘터차량 암호모듈 실종")
        if(int(result_67[i])==1):              #check Door sensor 
            if(int(result_67[i+1])==1):
                if(what_time_is_it(thistime, tmlst)):
                    red_list.append("67 쉘터차량 문열림")


    if(int(result_67[9])<=10):       #check ondo sensor
        red_list.append("67 쉘터차량 온도 낮음")
    elif(int(result_67[9])>28):
        red_list.append("67 쉘터차량 온도 높음")

    all = {'red':red_list}




    return render(request, 'blog/red.html',all)










def restart(request):
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










def league_stats(request):
    return render(request, 'blog/league_stats.html',{})
    