num=int(input("enter number you want"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("number is perfect")
else:
    print("number is not perfect")