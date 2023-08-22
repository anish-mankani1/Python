s=0
no=int(input("enter a number"))

while(no!=0):
    d=no%10
    s=s+(d*d*d)
    no=no/10
print(s)
if(no==s):
 print("it is armstrong")
else:
   print("not a armstrong number")
