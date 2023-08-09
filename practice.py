import random
user_choice=int(input("enter a 0 or rock and 1 for scisor and two for papaer"))
print(user_choice)
computer_choice=random.randint(0,2)
print(computer_choice)
while(user_choice>2):
 print("you have entered wrong choice")
 break
if(user_choice==0 and computer_choice==2):
 print("user wins")
elif(computer_choice==0 and user_choice==2):
 print("computer wins")
elif(user_choice>computer_choice):
 print("user wins")
elif(computer_choice>user_choice):
 print("computer wins")
 

