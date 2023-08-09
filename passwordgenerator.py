import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l''m','n','o','p','q','u','v','w','x','y','z']
symbol=['@','#','$','%','&','*','()']
number=['1','2','3','4','5','6','7','8','9']
print("welcome to passwor generator")
letter_list=int(input("how mnany letters do you want"))
symbol_list=int(input("how mnany letters do you want"))
number_list=int(input("how mnany letters do you want"))
password_list=[]
for i in range(1,letter_list+1):
    char=random.choice(letter)
    password_list+=char
for i in range(1,symbol_list+1):
     char=random.choice(symbol)
     password_list+=char
for i in range(1,number_list+1):
      char=random.choice(number)
      password_list+=char
print(password_list)
random.shuffle(password_list)
print(f"in shuffle form{password_list}")
password=""
for i in password_list:
     password+=i
print(password)


