print("1,sum","2.REv","3.palindrome")
f=int(input("choose..."))
if(f==1):
    i=int(input("no sum"))
    summ=0
    while i>0:
        c=i%10
        summ=summ+c
        i=i//10
    print("sum",summ)
elif(f==2):
    rev=0
    i=int(input("EBETR REV"))
    while i>0:
        c=i%10
        rev=c+rev*10
        i=i//10
    print("rev",rev)
elif(f==3):
    i=int(input("pali : "))
    chk=i
    rev=0
    while i>0:
        c=i%10
        rev=c+rev*10
        i=i//10
    if(chk==rev):
        print("palindrome")
    else:
        print("Not palindrome")

else:
    print("invalid chooices")