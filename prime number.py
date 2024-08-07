n=int(input("enter a value:"))
if(n>1):
    c=n**0.5
    for i in range(2,c+1):
        if(n%i==0):
            print("prime number")
        else:
            print("not a prime number")
