import random
easy_attempt=10
hard_attempt=5
def set_dificulty(level):
    if(level=='easy'):
        return easy_attempt
    else:
        return hard_attempt
    
def check_number(guessed_number,answer,attemps):
    if(guessed_number<answer):
        print("ypu have output is low")
        return attemps-1
    elif(guessed_number>answer):
        print("you have output is high")
        return attemps-1
    else:
        guessed_number==answer
        print("your guess is right")
        

print("any random number between 1 to 50")
answer=random.randint(1,50)
print(answer)#30
level=input("enter the dificulty level easy or hard ")
attemps=set_dificulty(level)#easy hai toh 10
guessed_number=0
while(guessed_number!=answer):#agar equal nahi hai toh - hota jahega
 print(f"you have this attemps {attemps} left ")
 guessed_number=int(input("enter a guesed number"))#agar 9 enter kiya
 attemps=check_number(guessed_number,answer,attemps)