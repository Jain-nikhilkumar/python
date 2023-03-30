f=open("ni.jpeg","rb")
f2=open("ni2.png","wb")

f2.write(f.read())
print("Done")