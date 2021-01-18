import mysql.connector

def getAll():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="spectrum")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `tbl_attendance`")

    myresult = mycursor.fetchall()
    return myresult
    #for x in myresult:
    #    print(x)

strTable = ("<html>"
"<head>"
"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'>"
"<link rel='stylesheet' type='text/css' href='https://cdn.datatables.net/1.10.23/css/jquery.dataTables.css'>"
"<script src='https://code.jquery.com/jquery-3.5.1.js'></script>"
"<script type='text/javascript' charset='utf8' src='https://cdn.datatables.net/1.10.23/js/jquery.dataTables.js'></script>"

"<script src='https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js'></script>"

"</head>"
"<body>"
"<div class='container'>"
"<div class='row'>"
"<h1>Web Portal</h1>"
"<table id='example' class='display' style='width:100%'>"
"<thead><tr><th>SL/NO</th><th>Name</th><th>date</th><th>Check IN</th><th>check Out</th></tr></thead>"
"<tbody>"
)

dataset=getAll()

for col in dataset:
    #print(col)
    strRW = "<tr><td>"+str(col[0])+ "</td><td>"+str(col[1])+ "</td><td>"+str(col[2])+ "</td><td>"+str(col[3])+ "</td><td>"+str(col[4])+"</td></tr>"
    strTable = strTable+strRW

strTable = strTable+"</tbody></table> </div> </div></body></html>"
strTable=strTable+"<script> $(document).ready(function() {$('#example').DataTable();} );</script>"
hs = open("index.html", 'w')
hs.write(strTable)

print (strTable)