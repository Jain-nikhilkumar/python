


class Below(Exception):
    pass

class Above(Exception):
    pass

i=int(input("Enter your marks..."))
try:
    if(i<0):
        raise Below
    elif(i>100):
        raise Above
    else:
        print("ENTERED MARKS ARE...",i)

except Below:
    print("MARKS ABE NOt VALID MARKS LESS THAN ZERO")
except Above:
    print("MARKS Are not VALILD MARKS above 100 ")
