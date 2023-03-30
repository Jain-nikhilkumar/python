s1={1,2,3,4,5}
s2={1,4,3,6,7,78}
print("SET 1",s1)
print("SET 2",s2,"\n\n")

print("1.Intersaction ","2.Uninn","3.difference")

i=int(input(""))
if i==1:
    print("Intersection is \n",s1.intersection(s2))

elif i==2:
    print("Unionn is \n",s1.union(s2))
elif i==3:
    print("Diffferencce of ",s1.difference(s2))
else:
    print("Invalid chooice..")