# snake water and gun game
import random
list=['s','w','g']
chances=5
no_of_chance=0
computer_points=0
human_point=0
print("\t \t \t snake water gun game ")
print("s for snake\n  w for water \n  g for gun\n")

# making game with the help of while loop
while(no_of_chance<chances):#0<5
    user=input("enter what do you want snake water gun:\n")
    _random=random.choice(list)

    if(user==_random):
        print("it's a tie both will get 1 point\n")

        #if user enter snake
    elif(user=="s" and _random=="w"):
        human_point=human_point+1
        print("human wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")


    elif(user=="s" and _random=="g"):
        computer_points=computer_points+1
        print("computer wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")

        #if user enter gun
    elif(user=="g" and _random=="w"):
        computer_points=computer_points+1
        print("computer wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")


    elif(user=="g" and _random=="s"):
        human_point=human_point+1
        print("human wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")
        
        #if user  enter water
    elif(user=="w" and _random=="s"):
        computer_points=computer_points+1
        print("computer wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")


    elif(user=="w" and _random=="g"):
        human_point=human_point+1
        print("human wins")
        print(f"human choice {user} and computer choice is {_random}\n")
        print(f"computer points are {computer_points} and human points are {human_point}\n")


    else:
        print("you have entered wrong choice")
    no_of_chance+=1
    print(f"{chances-no_of_chance} is left out {chances}\n")

print("game over")


if(human_point==computer_points):
    print("it's a tie both have same points")
elif(human_point>computer_points):
    print("you have won this match")
elif(human_point<computer_points):
    print("computer have won this match have won this match")
    #snake water gun game
    # snake drinks the water,thegun killed the snake and does not have any effect on water
        

        
        

        


        


        


        


        




