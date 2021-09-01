#read file using object
try:
    f=open("test.txt",'r',encoding='utf-8')
    print(f.read())
except:
     print("Not available")
finally:
    f=open("test.txt",'r',encoding="utf-8")
    f.close()