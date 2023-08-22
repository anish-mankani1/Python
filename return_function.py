#def format(f_name,l_name):
 #   name=f_name.title()
  #  last_name=l_name.title()
   # return name,last_name



#print(format("anish","MANKANI"))
def add(a,b):
  if(a==0 and b==0):
    return "you have entered wrong choice"
  else:
    return a+b
 

var1=int(input("enter the first value"))
var2=int(input("enter the second value"))
result=add(var1,var2)
print(result)