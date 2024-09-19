list2=[1,2,3,4,7,8,9]
n=len(list2)
print(n)
list4=[]

list3=[]
max=list2[0]
print(max)

for i in list2:
    if i>max:
        max=i
print(max)
    
min=list2[0]
print(min)

for i in list2:
    if i<min:
        min=i
for i in range(min,max):
    if i not in list2:
        list4.append(i)
print(list4)


