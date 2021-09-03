
#"create table stdinfo ( Name varchar (50),Address varchar (100),DeptNo int(5),studid varchar (20))"

import MySQLdb
try:
   
    query1="insert into stdinfo values('Nikhil','dhule','5','d662989j9')"  
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