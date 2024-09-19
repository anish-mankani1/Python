num=int(input("enter bnumber you want"))
while(num>0):
    i=num%10
    if(i!=0 and i!=1):
        print("not a binary number")
        break
    num=num//10
    print("num is ",num)
    if(num==0):
        print("number is  binary")