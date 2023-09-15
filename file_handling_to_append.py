#append mode mean to open a file in append/write mode
#write means it will erase the previous content the file pointer anywhere you want
#using seek operation we can move file poinet anywhere we want
#it will append at the end of the file means add something in the end
f1=open("file_4","a")#it will create new file
f1.write("hello student")
f2=open("file_2","a")
f2.write("hello anish")#it will also add in another file
#f1.read()#it will give error it will only use to write in append mode
f3=open("file_5","a")