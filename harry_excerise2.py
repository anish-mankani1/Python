#n=18
print("enter a number you want")
n=int(input("enter a number"))
print("guess the number is the game ")
no_of_guesses=1
while(no_of_guesses<9):
    guess_number=int(input("guess the number "))
    if(guess_number>n):
        print("you have entered number that is too high")
    elif(guess_number<n):
        print("you have entered the number that is too low")
    else:
        print("you won")
        print(no_of_guesses," chances you took to guess a number")
        break
    print(9-no_of_guesses,"you have left")
    no_of_guesses= no_of_guesses+1    #1+1=2

if(no_of_guesses>9):
    print("game over")

