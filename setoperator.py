#operator in set union and intersection
#union will not print duplicate value
#intersection will print only duplicate value
#union
set1={'anish','hemant','rohit'}
set2={'kudi','nisha'}
set3={'salman','lawrence'}
print(set1.union(set2,set3)) #it will print alltogether
print(set1.union(('mohan','suman'))) #it will convert tuple into set
set1.update(['anish','reshma'])#list into set
#intersection
set4={'ram','shyam','jenny'}
set5={'jenny','jiya','aakash'}
set6={'ankur','prateek'}
print(set4.intersection(set5)) #intersection will print only repeated value
print(set4.intersection(set5,set6))#it will give only empty set