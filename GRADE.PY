m1=int(input("enter the mark1:"))
m2=int(input("enter the mark2:"))
m3=int(input("enter the mark3:"))
total=m1+m2+m3
average=total/3
if(average>=90 and average<=100):
    print("Average:",average)
    print("you got S grade")
elif(average>=80 and average<90):
    print("Average:",average)
    print("you got A grade")
elif(average>=70 and average<80):
    print("Average:",average)
    print("you got B grade")
elif(average>=60 and average<70):
    print("Average:",average)
    print("you got C grade")
elif(average>=50 and average<60):
    print("Average:",average)
    print("you got D grade")
elif(average<50 and average>0):
    print("please enter valid input")
