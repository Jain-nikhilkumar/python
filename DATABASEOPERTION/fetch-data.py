import MySQLdb
try:
    query="select * from stdinfo"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    cur=myconn.cursor()
    cur.execute(query)

    tdata=cur.fetchall()
    print("The Records are ")
    for row in tdata:
        print("name : ",row[0])
        print("email : ",row[1])
        print("address : ",row[2])
except:
    print("data feached")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")
