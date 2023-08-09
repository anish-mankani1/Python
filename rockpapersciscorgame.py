import random
user_choice=int(input("enter 0 for rock and 1 for paper and 2 for sciscor "))
if(user_choice>=3):
  print("you have entered wrong choice")
else:
 computer_choice=random.randint(0,2)
print(computer_choice)
if(user_choice==computer_choice):
    print("it is draw")
elif(user_choice==0 and computer_choice==2):
    print("user wins")
elif(computer_choice==0 and user_choice==2):
    print("computer wins")
elif(user_choice>computer_choice):
    print("user wins")
elif(computer_choice>user_choice):
    print("computer wins")

