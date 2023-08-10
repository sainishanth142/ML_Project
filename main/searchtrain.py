import pandas as pd 
    
df = pd.read_csv("main/quora_duplicate_questions.csv")
ques1=list(df['question1'])
ques2=list(df['question2'])
print(ques1[0],ques2[0])
ques1=list(df['question1'])[:50]
ques2=list(df['question2'])[:50]
print(ques1[0],ques2[0])