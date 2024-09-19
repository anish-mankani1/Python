s="anish"

l=len(s)
print(l)


for i in range(l):
    found=True
    for j in range(l):
        if i!=j and s[i]==s[j]:  #g!g
            found=False
            break

    if found:
        print(i)
else:
    print("-1")
    


       
  
       
 