mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='Odia')

mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchone()
for i in result:
    print(i)