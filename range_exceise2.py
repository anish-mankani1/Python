#print number from  1 to 100 and if number is divisible by 3 then print fuzz and 5 
#print buzz and both then print fuzzbuzz otherwise print number
for i in range(1,16):

    if(i%3==0 and i%5==0):
       print("fizzbuzz")
    elif(i%3==0):
      print("fuzz")
    elif(i%5==0):
        print("buzz")
    else:
       print(i)