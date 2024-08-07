n=input("enter n: ")
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ"
b="0123456789"
s=0
c=0
for i in n:
    if i in a:
        c+=1
    else:
        s+=1
print("no. of letters: ",c)
print("no. of digits: ",s)

