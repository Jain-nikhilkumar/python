#11)program to find ASCII value of character
a = 'X'
print("The ASCII value of X is", ord(a))

a='x'
print("The ASCII value of x is", ord(a))


#12 Write Program to Compute Quotient and Remainder
a=4
b=8
print("Quotient: ",a//b)
print("Remainder",a%b)




#13)program to swap 2 no using temprary variable
X= input("Enter value of X:  ")
Y= input("Enter value of Y:  ")

temp=X
X=Y
Y=temp

print("The value of X after Swaping: ", X)
print("The value of Y after Swaping: ", Y)

#14)program to check no is odd or even

check=int (input("Enter a number: "))
if (check % 2)  ==  0 :
    print("it is EVEN no",check)
else:
     print("it is ODD no",check)



#15)PROGRAM O CHECK WHETHER AN ALPHABET IS VOWEL OR CONSONANT USING IF ....ELSE
X='I'

if X in ('a','e','i','e','u') :
    print("The given Alphabet is vowel",X)
else:
    print("The given Alphabet is consonant",X) 



#16)PROGRAM TO CALCULATE GST of 18% on baseprice of 34900


GST =((18/100) * 34900)

print ("GST is :",GST)


#17)PROGRAM TO CALCULATE MONTHLY SIMPLE INTREST AND COMPOUND INTREST (5%/MONTH)ON AMOUNT -161258/--

a=161258
r=5
t=1
si=a*r*t*0.01

print("SIMPLE INTRERST IS :",si)

AMOUNT=a*(pow((1+ r/100), t))
ci= AMOUNT - a
print("COMPOUND INTREST IS: ", ci)

#18)Program to calculate simple intrest and cvoumound intrest (5%/month) n amount -161258
a=161258
Y3=a/36
Y5=a/60

EMI3=Y3+(0.05*Y3)
EMI5=Y5+(0.05*Y5)

print("EMI FOR 3 YEARS WITH INREST5%:",EMI3)
print("EMI FOR 5 YEARS WITH INREST5%:",EMI5)




