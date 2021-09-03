import MySQLdb
try:
   
    query1="DROP TABLE stdinfo"  
    print("TABLE UPDATED SUCCESSFULLY")
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    cur=myconn.cursor()
    print("CURSOR......")
    cur.execute(query1)
    myconn.commit()
    print(query1,"table updated")
    
except:
     print("values updated")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")