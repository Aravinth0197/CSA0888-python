n=int(input("enter the decimal number:"))
binary=0
j=1
while(n!=0):
    i=n%2
    binary=binary+(i*j)
    n=n//2
    j*=10
print("binary:",binary)
