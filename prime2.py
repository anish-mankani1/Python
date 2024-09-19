def sum(no):
    i=2
    flag=0
    while(i<no):
        if(no%i==0):
         flag=1
         break
    if(flag==0):
        print("prime number")
    else:
        print("not a prime number")  
sum(5)


   