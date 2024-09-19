list1=[1,2,3,4,3,1,2,3,6,7,8]
n=len(list1)
print(n)
list2=[]
for i in range(n):
    print(i)
    if i in list1:
        list2.append(i)

print(list2)

