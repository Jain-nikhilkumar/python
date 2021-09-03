import MySQLdb
try:
   
    query1="create table stdinfo ( Name varchar (50),Address varchar (100),DeptNo int(5),studid varchar (20))"
    print("TABLE CREATED SUCCESSFULLY")
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    cur=myconn.cursor()
    cur.execute(query1)
    myconn.commit()
    print(query1,"table created")
    
except:
     print("Database updated")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")