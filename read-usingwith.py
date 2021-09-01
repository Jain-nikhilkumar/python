  
#read using with 
with open("test.txt",'r',encoding='utf-8') as f:
     print(f.read())
     f.close()