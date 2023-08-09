weight=float(input("enter weight"))
height=float(input("enter height"))
sum=weight/height**2
if(sum<18):
    print("you are underweight")
elif(sum<25):
    print("you are normal weight")
elif(sum<30):
    print("you arw overweight")
else:
    print("you are obessed")
#elif aise likhte hai python mein
