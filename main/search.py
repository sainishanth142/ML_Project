import nltk
import json
import features
# 11120
import pandas as pd 
    
df = pd.read_csv("main/quora_duplicate_questions.csv") 
ques1=list(df['question1'])
ques2=list(df['question2'])
for i in ques2:
    ques1.append(i)
# text=input().split()
# print(nltk.pos_tag(text))
browsers=['brave','edge','chrome']

done=0
for text in ques1[50000:]:
    try:
        text="open brave and search for "+text
        text=text.split()
        if("search" in text):
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
                if(i=='search'):
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
            # print("--------------Previous Results------------------")
            # k=-1
            # for i,j in enumerate(resultpre):
            #     print(str(i+1)+" "+j)
            #     k=i
            result=(features.google.search(search_term))
            
            # print("--------------Search Results------------------")
            # for i,j in enumerate(result):
            #     print(str(k+i+1+1)+" "+j)
            # print("--------------------------------")
            # opt=int(input("select an option : "))-1
            opt=1
            for i in resultpre:
                result.append(i) 
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
        continue
    done+=1
    print(done)

        


    

