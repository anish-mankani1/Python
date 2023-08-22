a=10
def display():
  global a# by using this keyword we can do anything to global scope
  a=a+1
  print(a)
display()  
