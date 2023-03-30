l=[]
print("list after before elements",l)
t=(1,2,3,4,5)
l.extend(t)
print("list after adding elements",l)
i=int(input("enter element to remove"))
l.remove(i)
print("list after removinig elements",l)

f=int(input("enter element to find :"))

for ele in l:
    if(ele==f):
        flag=1
        break
    else:
        flag=0  

if(flag==1):
    print("FOUNF")
else:
    print("NOT FOUND")