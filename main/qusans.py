import pandas as pd 
import features
df = pd.read_csv("main/quora_duplicate_questions.csv") 
ques1=list(df['question1'])
ques2=list(df['question2'])
for i in ques2:
    ques1.append(i)

for i in ques1:
    ans=features.chatgpt().get(i)
    print(ans)