#17)PROGRAM TO CALCULATE MONTHLY SIMPLE INTREST AND COMPOUND INTREST (5%/MONTH)ON AMOUNT -161258/--

a=161258
r=5
t=1
si=a*r*t*0.01

print("SIMPLE INTRERST IS :",si)

AMOUNT=a*(pow((1+ r/100), t))
ci= AMOUNT - a
print("COMPOUND INTREST IS: ", ci)