f1=open("file_1","r+")# in this mode first read and then write
print(f1.tell())
#print(f1.read())
#f1.write("this is python course")
f1.write("hi")# we can first write also then read
print(f1.tell())
print(f1.read())#the ans start from lcome because the file pointer is in at bignning
#in r+ mode then it will overwrite we with hi
print(f1.tell())

# in r+ mode we have to first read an then write
#tell() it will tell us about file pointer position
# idhar hi overwrite hogaya hi sehi
#*******************************************************