import pandas as pd
import numpy as np

df = pd.read_excel (r'sample__AttendanceLog__2016.xlsx').fillna(0).to_numpy()
num_rows, num_cols = df.shape
print(num_cols)
print(num_rows)
i=0



p=0
while True:
    if(p>=5):break
    k=0
    while True:
        #print(i)
        if(k+3>num_rows): break
        if(df[1+k,2+p]==0): 
            k=k+1
            continue
        print("Name:"+df[0,2+p])
        print("Date:"+str(df[1+k,0]))
        print("In:"+str(df[1+k,2+p]))
        print("Out:"+str(df[2+k,2+p]))
        k=k+2
        i=i+1
    p=p+1


"""
m=0
j=1
while True:
    if(m>=4):
            break
    #single row data fetching from 2d array 
    i = 0
    while True:
        if(i+3>num_cols):
            break
        
        print(j)
        print("Name:"+df[m+3,1])
        print("Date:"+str(df[1,i+2]))
        print("In:"+str(df[m+3,i+2]))
        print("Out:"+str(df[m+3,i+3]))
        j=j+1
        i=i+2
    m=m+1
"""

#print (df[:,6])
