n=input("enter n: ")
c=0
p=0
for i in reversed(n):
    c+=int(i)*(2**p)
    p+=1
print(c)
