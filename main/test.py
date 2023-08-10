import firebase_admin
from firebase_admin import db
import json
import features
import subprocess,os
class googlesearch():
    def search(self,text):
        output = "Please ask a question"
        browsers=['brave','edge','chrome']
        try:
            text=text.split()
            if(1):
                with open(r"C:\Users\saini\Desktop\mlproject\data\browsingdata.json", 'r') as openfile:
                    json_object = json.load(openfile)
                default_browser=json_object['default_browser']
                if(default_browser not in browsers):
                    selected_browser=''
                else:
                    selected_browser=default_browser
                for i in browsers:
                    if i in text:
                        selected_browser=i
                
                if(selected_browser==''):
                    print("Please select a browser")
                    print("1-brave")
                    print("2-edge")
                    print("3-chrome")
                    selected_browser=browsers[int(input())-1]
                    default_browser=selected_browser
                    with open(r"C:\Users\saini\Desktop\mlproject\data\browsingdata.json", "w") as outfile:
                        json.dump({'default_browser':default_browser}, outfile)
                search_term=''
                
                y,z=False,True
                for i in text:
                    if(i.lower()=='search'):
                        y=True
                        continue
                    if(y):
                        if(z):
                            if(i=='for'):
                                z=False
                                continue
                        search_term+=i+" "
                k=0
                
                for i in search_term.split()[::-1]:
                    for j in browsers:
                        if j==i:
                            k=1
                            break
                if(k):
                    search_term=' '.join((search_term.split()[:len(search_term.split())-2]))
                resultpre=[]
                with open(r"C:\Users\saini\Desktop\mlproject\data\searchdata.json", 'r') as openfile:
                    searchdata = json.load(openfile)
                
                if(search_term in searchdata.keys()):
                    resultpre=searchdata[search_term].keys()
                print("--------------Previous Results------------------")
                k=-1
                for i,j in enumerate(resultpre):
                    print(str(i+1)+" "+j)
                    k=i
                result=(features.google.search(search_term))
                
                print("--------------Search Results------------------")
                for i,j in enumerate(result):
                    print(str(k+i+1+1)+" "+j)
                print("--------------------------------")
                # opt=int(input("select an option : "))-1
                opt=0
                output="previous results: <br>"
                for i in resultpre:
                    output+="<a target='_blank' href='"+i+"'>"+i+"</a>"+" <br>"
                output+="search results: <br>"
                for i in result:
                    output+="<a target='_blank' href='"+i+"'>"+i+"</a>"+" <br>"

                for i in resultpre:
                    result.append(i) 
                print(output)
                # webUrl = urllib.request.urlopen(result[opt]) 
                data=searchdata 
                for i,j in enumerate(result):
                    try:
                        if(search_term not in searchdata.keys()):
                            data[search_term]={}
                        if(i==opt):
                            if(j in searchdata[search_term].keys()):
                                data[search_term][j]+=1
                            else:
                                data[search_term][j]=1
                        else:
                            if(j in searchdata[search_term].keys()):
                                continue
                            else:
                                data[search_term][j]=0
                    except Exception as e:
                        print(e)
                        continue
                with open(r"C:\Users\saini\Desktop\mlproject\data\searchdata.json", "w") as outfile:
                    json.dump(data, outfile)
        except Exception as e:
            print(e)
        return output

cred_obj = firebase_admin.credentials.Certificate('main/cred.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':"https://home-automation-6d220-default-rtdb.firebaseio.com/"
    })
refc=db.reference("/")
ref=db.reference("/question/")
applicationslist={'arduino':{'path':r"C:\Users\saini\AppData\Local\Programs\Arduino IDE\Arduino IDE.exe"},'brave':{'path':r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"},'calculator':{'path':r"C:\\Windows\\System32\\calc.exe"},'notepad':{'path':r"C:\\Windows\\System32\\notepad.exe"},"draw":{'path':r"C:\Program Files\draw.io\draw.io.exe"}}
pwd=r"C:\Users\saini\Desktop\mlproject"
try:
    while True:
        if(ref.child('done').get()==0):
            print(ref.child('value').get())
            MyText=ref.child('value').get()
            if("search" in MyText.split(" ")):
                # ans=googlesearch().search(MyText)
                # refc.set(ans)
                output=googlesearch().search(ref.child('value').get())
                refc.child("output").set(output)
                ref.child('done').set(1)
            if("open" in MyText.split(" ")):
                for i in applicationslist:
                    if(i in MyText):
                        app=subprocess.Popen(applicationslist[i]["path"]) 
                        applicationslist[i]["process"]=app
                        refc.child("output").set(i+" is opened")
                        ref.child('done').set(1)
            if("close" in MyText.split(" ")):
                for i in applicationslist:
                    if(i in MyText):
                        applicationslist[i]["process"].kill()
                        refc.child("output").set(i+" is closed")
                        ref.child('done').set(1)
            if("go to" in MyText):
                if("previous" in MyText):
                    features.lap.pretab()
                    refc.child("output").set("Done")
                    ref.child('done').set(1)
                if("next" in MyText):               
                    features.lap.posttab()  
                    refc.child("output").set("Done ")
                    ref.child('done').set(1) 
            if("navigate" in MyText):
                if("previous" in MyText):
                    mes=""
                    for k in os.listdir("\\".join(pwd.split("\\")[:len(pwd.split("\\"))-1])):
                        print(k)
                        mes+=k+"<br>"
                    pwd="\\".join(pwd.split("\\")[:len(pwd.split("\\"))-1])
                    refc.child("output").set(mes)
                    ref.child('done').set(1)
                if("into" in MyText):
                    mes=""
                    s=MyText.split("to ")[-1]
                    pwd+="\\"+s  
                    for k in os.listdir(pwd):
                        print(k)
                        mes+=k+"<br>"
        
                    refc.child("output").set(mes)
                    ref.child('done').set(1)
            if("create" in MyText):
                mes=""
                f=MyText.replace("create ","")
                f=f.replace(" folder","")
                os.mkdir(pwd+"\\"+f)
                for k in os.listdir(pwd):
                        print(k)
                        mes+=k+"<br>"
                refc.child("output").set(f +" folder is created<br>"+mes)
                ref.child('done').set(1)
except Exception as e:
    print(e)