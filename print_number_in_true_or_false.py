print("how many row you want to print")
one=int(input("enter a number"))
print("type 1 or 0")
two=int(input("enter number 0 or 1"))
new=bool(two)
print(new)
if new==True:
    for i in range(1,one+1):# 1 and 5 matlab 1 se lekar 4
        print(i)
        for j in range(1,i+1):#1 se lekar 2 matlab ek hi print hoga
            #j row ke liye hota hai aur i column ke liye
            print("*",end=" ")
        print()

elif new==False:
   for i in range(one,0,-1):#4 se 0 steps =-1
       for j in range(1,i+1):
              print("*",end=" ")
       print()