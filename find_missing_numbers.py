def fun(numbers):
    max=numbers[0]
    print(max)   1

    for i in numbers:
        if(i>max):
            max=i
    print(max)      9

    min=numbers[0]           1
    print(min)

    for i in numbers:
        if(i<min):
            min=i
    print(min)

    list1=[]

    for i in range(min + 1, max):   2 se 9
        if i not in numbers:
          list1.append(i)
    return(list1)


numbers= [1,2,3,5,7,8,9]
print(fun(numbers))