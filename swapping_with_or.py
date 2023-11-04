a=int(input("enter number"))
b=int(input("enter number"))
print(a,"before swapping")
print(b,"before swapping")
a=a^b
b=a^b
a=a^b
print(a,"after swapping")
print(b,"after swapping")