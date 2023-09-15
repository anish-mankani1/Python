x=[]
for i in range(10):
    no=int(input("enter 10 number"))
    x.append(no)
a=int(input("enter the number you want to search"))
for i in range(10):
           if(x[i]==a):
               p=i+1
               print(p)
           elif(x[i]!=a):
                 print("you have entered wrong choice")
                 break

