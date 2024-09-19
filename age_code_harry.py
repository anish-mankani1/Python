age=int(input("enter your age or year "))
isage=False
isyear=False
if(len(str(age==4))):
    isyear=True
else:
    isage=True

if(age<1900 & isyear):
    print("you seems to be the oldest person on the planet ")
if(age>2024):
    print("you are yet to bornv")

if isage:
    age= 2024 -age


print(f"your age after 100 year will be {age + 100}")

interestedage=int(input("enter age do you want to know"))
print(f"you will be {interestedage- age} years old {interestedage}")