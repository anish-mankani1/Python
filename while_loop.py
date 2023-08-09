#while loop with else.else executed when while loop is false
count=1
#while(count<=5):
 #   print(count)
  #  count+=1
#else:
#    print("in else block")
#print("out of loop")
while(count<=5):
    print(count)
    count+=1
    if(count==3):
        break
else:#here else block does not executed because of forcefully termination
    print("in else block")