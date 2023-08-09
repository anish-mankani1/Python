set1={1,True,'jenny',1.11}  #DUPLICATE ARE NOT ALLOWED 1 and true
print(set1) #they are unordered
print(type(set1))
set2={}
print(type(set2)) #we have created empty dictionary
set3=set()
print(type(set3))      #we have creatd empty set
set1.add(99)
print(set1)
print(len(set1)) # 4 because 1 and true are duplicate values
set4={1,2,3,4,5,6,1} #it will give ans 2,3,4,5,6 and 1 is duplicate and duplicate are not allowed
set4.remove(1)
print(set4)
set4.discard(1)
print(set4)   # discard=remove
set5={1,'jenny',10.11,True,45,78}
print(set5.pop()) #pop will remove any random number
print(set5)
set6={1,2,3,4,5,6,7}
set6.add((67,78,98))
print(set6) #tuples can add because they are immutable
           #list can not add becausse they are mutable