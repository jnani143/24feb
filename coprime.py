num=int(input('enter number'))
c=0
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        c=c+1
print(c)
