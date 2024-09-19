str=input("enter string you want ")
ch=input("enter character you want to replace with space ")
str1=""
for i in range(len(str)):
    if(str[i]==' '):
        str1+=ch
    else:
        str1+=str[i] 
print(str1)