# differnce and symmetric difference in python

set1={'ram','shyam','jenny'}
set2={'jenny','jiya','aakash'}
set3={'ankur','pradeep','ram'}
#print(set1.difference(set2)) #it will print difference between them
#print(set1-set2)
#print(set1.difference(('mohan','riya')))#tuple into set
#print(set1.difference(set2,set3)) #it will give shyam because in first case properties
# will come left to right difference between set1 and set2  and ans is {'ram',shyam}
# and then set1 and set3 it contain only ram
#set1.difference_update(set2)
#print(set1)#it will give non-repeated value
#symmetic difference in set
print(set1.symmetric_difference(set2)) #it will give non repetable value
#combination of union and intersection
#it will contain  only one argumnet
set1.symmetric_difference_update(('hemant','raina'))
print(set1)