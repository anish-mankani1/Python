f2=open("file_3","w+")
print(f2.tell())
print(f2.write("hi my name is jenny"))
print(f2.tell())
print(f2.write("this is python course"))
print(f2.tell())
f2.seek(0)#0 means from starting
print(f2.tell())
data=f2.read()
print(data)
print(f2.tell())
f2.close()#it is optional

