t=(11,2,11,4,5,5,66,7,8,8)
s=set()
for k in t:
    if(t.count(k)>1):
        s.add(k)
print("Reapted values are",s)

tup=("ZERo","one","two","three","four","five","six","seven","eight","nine","ten")
i=int(input("enetr no"))
wi=[]
while i>0:
    c=i%10
    i=i//10
    wi.append(tup[c])
wi.reverse()

for k in wi:
    print(k,end=" ")
