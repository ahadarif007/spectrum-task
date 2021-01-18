import pandas as pd
import numpy as np
import mysql.connector

def insert(name,date,checkIn,checkOut):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="spectrum"
        )
    mycursor = mydb.cursor()
    sql="INSERT INTO `tbl_attendance`(`Name`, `Date`, `check-In`, `check-out`) VALUES (%s,%s,%s,%s)"
    val = (name,date,checkIn,checkOut)
    mycursor.execute(sql, val)
    mydb.commit()


data_frames = pd.read_excel (r'sample__AttendanceLog__2016.xlsx',sheet_name=None)

records=1
for d in data_frames:
    print("sheet("+str(records)+") : "+d+" Processing....")
    records=records+1
    df=data_frames.get(d).fillna(0).to_numpy()
    num_rows, num_cols = df.shape
    #print(num_cols)
    #print(num_rows)
    
    if(num_cols<10):
        p=0
        while True:
            if(p>=5):break
            k=0
            while True:
                if(k+3>num_rows): break
                if(df[1+k,2+p]==0): 
                    k=k+1
                    continue
                #insert(str(df[0,2+p]),str(df[1+k,0]),str(df[1+k,2+p]),str(df[2+k,2+p]))
                print("Name:"+df[0,2+p]+" Date:"+str(df[1+k,0])+" In:"+str(df[1+k,2+p])+" Out:"+str(df[2+k,2+p]))
                #print("Name:"+df[0,2+p])
                #print("Date:"+str(df[1+k,0]))
                #print("In:"+str(df[1+k,2+p]))
                #print("Out:"+str(df[2+k,2+p]))
                k=k+2
            p=p+1
    else:
        m=0
        #j=1
        while True:
            if(m>=4):
                    break
            i = 0
            while True:
                if(i+3>num_cols):
                    break
                insert(str(df[m+3,1]),str(df[1,i+2]),str(df[m+3,i+2]),str(df[m+3,i+3]))
                #print("Name:"+df[m+3,1]+" Date:"+str(df[1,i+2])+" In:"+str(df[m+3,i+2])+" Out:"+str(df[m+3,i+3]))
                #print("Name:"+df[m+3,1])
                #print("Date:"+str(df[1,i+2]))
                #print("In:"+str(df[m+3,i+2]))
                #print("Out:"+str(df[m+3,i+3]))
                #j=j+1
                i=i+2
            m=m+1