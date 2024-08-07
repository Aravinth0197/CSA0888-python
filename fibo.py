n=int(input("enter n: "))
a=0
b=1
f=[0,1]
for i in range(2,n):
    c=a+b
    a=b
    b=c
    f.append(c)
print(f)
