f1=open("file_1","a+")#if file does not exist we a+ create new file
print(f1.tell())
f1.seek(0)
print(f1.read())#read isliye nahi hoga kyu ki file pointer ka cursor hameshaa
#akhri mein hota hai we can notable  to read
f1.write("jenny's lecture")
print(f1.read())