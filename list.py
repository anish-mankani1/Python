number=[1,2,3,4,5,2]
names=["anish","jenny","hemant"]
mix=[1,"anish","true",10.10]
str={"anish mankani","hemant","rohit"}
print(number)
print(names)
print(mix)
print(number[0])
print(len(number))
print(number[-1])
#slicing in list
print(number[1:3])
print(number[0:5:2])
number.sort()
print(number)
print(number.sort())
print(min(number))
print(max(number))
number.reverse()
print(number)
#mix.sort()
#print(sort)
number.append(45)
print(number)
number.insert(2,45)
print(number)
#by using append and insert we can add only one data at a time
#by using extend we can more than one data at a time
number.extend([45,46,47,48,49,50])
print(number)
number[0]=67
print(number)
number[0:4]=[67,68,69]
print(number)
number.remove(67)
print(number)
#pop will remove first and return last elmenet ex 1,2,0,3,4,0
#it will guve ans 1,2,3,4,0 remove first elemnet
#it will also remove p[articular elemnet
number.pop(11)
print(number)
