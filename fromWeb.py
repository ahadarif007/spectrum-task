
import mysql.connector
import datetime
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def insert(name,date,checkIn,checkOut):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="spectrum")
    mycursor = mydb.cursor()
    sql="INSERT INTO `tbl_attendance`(`Name`, `Date`, `check-In`, `check-out`) VALUES (%s,%s,%s,%s)"
    val = (name,date,checkIn,checkOut)
    mycursor.execute(sql, val)
    mydb.commit()

scope = [   'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'spectrum-302020-761e674e714f.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1rxZwyZp9tsDTd_Q82LdO22XdjqZr14vNvbNKAY7jQYU/edit#gid=838827690')


wks_list = wks.worksheets()

#print(wks_list)

for ws in range(len(wks_list)):
    #print(ws)
    data = wks.get_worksheet(ws).get_all_values()
    headers = data.pop(0)

    df = pd.DataFrame(data, columns=headers).fillna(0).to_numpy()
    num_rows, num_cols = df.shape
    #print(num_cols)
    #print(num_rows)
    print(df)
    if(num_cols<10):
        p=0
        while True:
            if(p>=5):break
            k=0
            while True:
                if(k+3>num_rows): break
                if(df[1+k,2+p]==""): 
                    k=k+1
                    continue

                date_time_str = str(df[1+k,0])
                date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %b %d, %Y')
                insert(str(df[0,2+p]),date_time_obj,str(df[1+k,2+p]),str(df[2+k,2+p]))
                #insert(str(df[0,2+p]),str(df[1+k,0]),str(df[1+k,2+p]),str(df[2+k,2+p]))
                #if(str(df[0,2+p])=="Sanjoy"):
                #print("Name:"+df[0,2+p]+" Date:"+str(df[1+k,0])+" In:"+str(df[1+k,2+p])+" Out:"+str(df[2+k,2+p]))
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
            if(m>=5):
                    break
            i = 0
            while True:
                if(i+3>num_cols):
                    break
                if(m+3>=num_rows): break
                if(str(df[m+3,i+2])==""):
                    i=i+2
                    continue
                date_time_str = str(df[1,i+2])
                date_time_obj = datetime.datetime.strptime(date_time_str, '%a, %b %d, %Y')
                insert(str(df[m+3,1]),date_time_obj,str(df[m+3,i+2]),str(df[m+3,i+3]))
                #insert(str(df[m+3,1]),str(df[1,i+2]),str(df[m+3,i+2]),str(df[m+3,i+3]))
                #if(str(df[m+3,1])=="Sanjoy"):
                #print("Name:"+df[m+3,1]+" Date:"+str(df[1,i+2])+" In:"+str(df[m+3,i+2])+" Out:"+str(df[m+3,i+3]))
                #print("Name:"+df[m+3,1])
                #print("Date:"+str(df[1,i+2]))
                #print("In:"+str(df[m+3,i+2]))
                #print("Out:"+str(df[m+3,i+3]))
                #j=j+1
                i=i+2
            m=m+1
