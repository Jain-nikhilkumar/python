import MySQLdb
try:
   
    query1="update stdinfo set address='SOLAPUR' where name='Nikhil' "
    print("TABLE UPDATED SUCCESSFULLY")
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    cur=myconn.cursor()
    cur.execute(query1)
    myconn.commit()
    print(query1,"table updated")
    
except:
     print("Database updated")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")