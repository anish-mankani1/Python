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