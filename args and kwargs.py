#*args and **kwargs are argument 
#*args is a position argument
#**kwargs is a positional argument
#ex of *args                      #we can chose any name *a,*b
def add(a,*number,name):#normal,arbitary,keyword argument ek saath yeh hi order sahi hai
    c=0  
    print(name)      #the number will become tuple(5,6,7) because tuplle are immutable
    for i in number: #they can not change value can not change
     c=c+i
    print(c)
add(5,6,7,name="jennny")
#**kwargs is a keyword argument      #we can choose any  name
def person(**kwags):
   for key,value in kwags.items():#aise hi access hoga
      print(key,value)
person(name="anish",age=30,dept="cse")
person(name="anish",age=30,dept="cse")
