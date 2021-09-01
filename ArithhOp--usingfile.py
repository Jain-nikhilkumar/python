#3)Write programm to read file and make Arithematic operation using file content.(File attached : "arithmatic.txt")
f=open("arithmatic.txt",'r',encoding='utf-8')
x=f.readlines()
y=x[0].split()

add=0
sub=0
mul=0


for i in y:
   
    add = add + int(i)
    sub = sub - int(i)
    mul = mul * int(i)

print("\nAddition is: ",add)
print("\nSubtraction is: ",sub)  
print("\nMultiplication is: ",mul) 