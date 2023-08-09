list1=["hi","hello","welcome"]
list2=["krishna","ram","madhav"]
for i in list1:
    for j in list2:
        print(i,j)
        if(i=="hello" and j=="ram"):
            break
    print("out from inner loop")