num_1=int(input("enter the first number"))
num_2=int(input("enter the second number"))
print("+,-,*,%,/")
num_3=input("enter the operator")
if(num_1==45 and num_2==3 and num_3=='*'):
    print("555")
elif(num_1==56 and num_2==9 and num_3=='+'):
    print("777")
elif(num_1==56 and num_2==6 and num_3=='/'):
    print("4")
elif(num_3=='*'):
    num_4=num_1*num_2
    print(num_4)
elif(num_3=='+'):
    num_4=num_1+num_2
    print(num_4)
elif(num_3=='+'):
    num_4=num_1-num_2
    print(num_4)

