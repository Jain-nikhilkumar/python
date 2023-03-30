


Str="HELLO  mam"
def cal(Str):
    l=0
    u=0

    for k in Str:
        if(k.islower()):
            l+=1
        if(k.isupper()):
            u+=1
    print("u",u)
    print("l",l)
cal(Str)