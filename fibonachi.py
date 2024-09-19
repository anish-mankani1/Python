n=int(input("enter how number till you want to print  fibonachi  series "))
first,second=0,1
def function(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    else:
        return function(number-1) + (number-2)
    
for i in range(0,n):
    print(function(i))
    