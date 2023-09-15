def fusion(*args):
    for item in args:
     print(item)
data=["harry","manish","hem","rekha","savitri","munnni","shiela"]
fusion(data)
fusion(*data)

def facta(**kwargs):
   for key,values in kwargs.items():
      print(key,values)

#kwargs
date={"args":"it is function","anish":"he is anish","mama":"he is mama"}

facta(**date)
def anish(**kwargs):
   for item,system in kwargs.items():
      print(item,system)

data={"anish":"he is agood boy"}
anish(**data)