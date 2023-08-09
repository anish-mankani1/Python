# else block executed only and only if for loop succesfully excecuted it is not like in 
#c and c++ wher for loop executed and else does not  
#tuple1=(2,56,7,8,9)
#for i in tuple1:
 #   print(i)
  #  if(i==2):
   #   print(i) # we have forcefully executed from loop and else does not run
    #break
#else:
 #   print("succesfully completed")
tuple2=(1,9,7,5,4)
for i in tuple2:
    if(i%6==0):
      print(i)
    break
else:
    print("there is no number divible by three")