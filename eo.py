x=input()
l=x.split()
o=[]
e=[]
for i in range (len(l)):
    i=int(i)
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in range (len(o)):
    print(o[i],end=' ')
print(' ',end=' ')
for i in range (len(o)):
    print(o[i],end=' ')
