def sum(no):
    flag=0
    i=2
    while(i<no):
        if(no%i==0):
            flag=1
            break
        i+=1
    if(flag==0):
          print("prime")
    else:
      print("not a prime")


sum(5)