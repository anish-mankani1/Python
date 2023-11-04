number=int(input("enter the number you want"))
for i in range(1,number):
    if(i%3==0 and i%5==0):
        print("divisible by both")
    elif(i%3==0):
        print("divisible by 3")
    elif(i%5==0 ):
        print("divisible by 5")
    else:
        print(i)