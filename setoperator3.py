# isdisjoint and issubset
set1={'ram','shyam','jenny'}
set2={'jenny','jiya','aakash'}
set3={'ankur','pradeep','ram'}
print(set1.isdisjoint(set2))#disjoint means that it will opposite to each other
#does not contain same values
print(set1.isdisjoint(['mohan','rohan']))# now the ans is true because they are opposite 
#to each other
#subset mean set1 contain all the value of set2
print(set1.issubset(set2)) #ans is fale it contain different values
print(set1.issubset(('ram','shyam','jenny','romeo')))
#ans is true because it contain all the value of set1
print(set1.issubset(set1))#ans is true because every elemnet is subset of itself