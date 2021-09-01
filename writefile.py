#write file using object
try:
    f=open("test.txt",'w',encoding="utf-8")

    f.write("i am doing it late ")
except:
    print("try it again")
finally:
     f=open("test.txt",'w',encoding="utf-8")
     f.close()
