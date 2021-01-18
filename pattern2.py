import pandas as pd
import numpy as np

df = pd.read_excel (r'C:\Users\Ahad\Desktop\spectrum\sample__AttendanceLog__2016.xlsx', sheet_name='May 2016').fillna(0).to_numpy()
num_rows, num_cols = df.shape
#print(num_cols)
#print(num_rows)

m=0

j=1
while True:
    if(m>=5):
            break
    #single row data fetching from 2d array 
    i = 0
    while True:
        if(i+3>num_cols):
            break
        if(str(df[m+3,i+2])=="0"):
            j=j+1
            i=i+2
            continue
        print(j)
        print("Name:"+df[m+3,1])
        print("Date:"+str(df[1,i+2]))
        print("In:"+str(df[m+3,i+2]))
        print("Out:"+str(df[m+3,i+3]))
        j=j+1
        i=i+2
    m=m+1

#print (df)
