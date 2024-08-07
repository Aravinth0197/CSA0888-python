n=(3,6,8,9,8,9,12,35,8)
t=int(input("enter target: "))
c=0
for i in n:
    if t==i:
        c+=1
print(c)
