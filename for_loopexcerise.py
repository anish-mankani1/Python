height=input("enter heights separated by space")#height char mein aahegi
height_list=height.split(" ")
print(height_list)
count=0
for i in height_list: # count karege
      count =count+1
     
print(count)
for j in range(count):# range function use kiya
      height_list[j]=int(height_list[j])
print(height_list)#yaha char ko int kiya
total=0
for i in height_list:
      total+=i#154 155 160 167 142
print(total) #773
avg=total/count
print(avg)
print(round(avg)) # yaha round of kiya 154.6 to 155
