#f=open("anish2.txt","w")#it will overwrite prevoius content
#f.write("anish bhai bohot ache hai")
#a=f.write("anish bhai bohot ache hai")
#print(a)
#f.close()
f=open("anish2.txt","r+")
print(f.read())
f.write("thank you")
print(f.read())
