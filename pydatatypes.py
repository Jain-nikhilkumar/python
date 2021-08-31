# Write a program to manipulate List data

V=['red','blue','GREEN','pink','yellow',1,2,3,4,5]
print("\nList V :",V[:])

print("\nList V : 2 to 5",V[2:6])

print("\nList V in reverse:",V[::-1])

V.append('black2')
print("\nList V after appending  :",V[:])

V.insert(3,'greeen3')
print("\nList V after inserting  :",V[:])

V.pop(1)
print("\nList V after poping :",V[:])

V.remove('yellow')
print("\nList V after removing :",V[:])

del V[0]
print("\nList V after deleteing :",V[:])

V.clear()
print("\nList A after clearing :",V[:])

# Write a program to manipulate Tuple data

C=("red","green","yellow","blue","black","gray",101,102,103,104)

print("\nTuple C:",C)

print("\nTuple C: 2 to 5",C[2:6])

print("\nTuple C in reverse:",C[::-1])

print("\nCount of blue  is :",C.count('blue'))

# Write a program to manipulate List data

V=['white','Blue','red','green','Black',1,2,3,4,5]
print("\nList V :",V[:])

print("\nList V : 2 to 5",V[2:6])

print("\nList V in reverse:",V[::-1])

V.append('black2')
print("\nList V after appending  :",V[:])



# Write a program to manipulate tuple data

C=("green","red","black","pink","blue","white","yellow",101,102,103,104)

print("\nTuple C:",C)

print("\nTuple C: 2 to 5",C[2:6])

print("\nTuple C in reverse:",C[::-1])

print("\nCount of yellow is :",C.count('yellow'))