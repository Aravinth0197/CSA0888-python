b=input("enter binary number:")
decimal=0
power=0
for i in reversed(b):
    decimal+=int(i)*(2**power)
    power+=1
print(decimal)
