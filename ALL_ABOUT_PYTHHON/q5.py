a1=int(input("1stno "))
a2=int(input("2snnd"))

try:
    c=a1/a2
    print("division is :",c)
except ZeroDivisionError:
    print("DIVIDE BY ZERO IS RESTRICATTED...")