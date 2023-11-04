def parindrone(no):
    on=no
    r=0
    while(on>=0):
        d=int(no%10)
        r=(r*10)+d
        on=int(on/10)
    if(no==r):
        print("palindrone")
    else:
        print("not a palindrone")

no=int(input("enter what do you want"))
parindrone(no)