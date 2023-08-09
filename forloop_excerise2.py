number=input("enter the number separted by space")
number_list=number.split()
print(number_list)
count=0
for i in number_list:
    count+=1
print(f"the count of number is:{count}")
print(count)
for i in range(0,len(number_list)):
    number_list[i]=int(number_list[i])
print(number_list)
maximum_number=number_list[0]
for i in number_list:
 if(i>maximum_number):
    maximum_number=i
print(maximum_number)



