import numpy as np

fpr= open("D:\\survey.csv", "r")
line=fpr.readline()
while(len(line)>0):
    arr=line.strip().split(',')
    print(arr)
    line=fpr.readline()
fpr.close()

User_IDs=[]
Age=[]
Genders=[]
Platforms=[]
Daily_Usage_Times=[]
Posts_Per_Days=[]
Likes_Received_Per_Days=[]
Comments_Received_Per_Days=[]
Messages_Sent_Per_Days=[]
Dominant_Emotions=[]
fpr= open("D:\\survey.csv", "r")
head=fpr.readline()
line=fpr.readline()
while(len(line)>0):
    arr=line.strip().split(',')
    User_IDs.append(arr[0])
    Age.append(arr[1])
    Genders.append(str(arr[2]))
    Platforms.append(str(arr[3]))
    Daily_Usage_Times.append(arr[4])
    Posts_Per_Days.append(arr[5])
    Likes_Received_Per_Days.append(str(arr[6]))
    Comments_Received_Per_Days.append(str(arr[7]))
    Messages_Sent_Per_Days.append(str(arr[8]))
    Dominant_Emotions.append(str(arr[9]))
    line=fpr.readline()
fpr.close()
print(Likes_Received_Per_Days)
print(Age)
print(Dominant_Emotions)
print(Platforms)