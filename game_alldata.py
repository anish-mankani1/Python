import random
import game
print(game.game_logo)
print(game.vs)
import os
score=0

import game_data
#print(game_data.data)
def check_correct(follower_count1,follower_count2,guess):
    if(follower_count1<follower_count2):#20<50
        if(guess==1):#1==1
         return False
        else:#2
          return True
    else:
      if(guess==1):
         return True
      else:
         return False
flag=True
account_2=random.choice(game_data.data)#virat kohli
while flag==True:
      
 account_1=account_2#virat kohli
 account_2=random.choice(game_data.data)#virat kohli
 while(account_1==account_2):#virat kohli == virat kohli
    account_2=random.choice(game_data.data)#narendra modi
#print(account_1)
#print(account_2)

 name=account_1['name']
 descrption=account_1['descrption']
 country=account_1['country']
 print(f"compare 1: {name},{descrption},{country}")

 print(game.vs)#vs

 name=account_2['name']
 descrption=account_2['descrption']
 country=account_2['country']
 print(f" compare 2: {name},{descrption},{country}")

 follower_count1=account_1['follower']
 follower_count2=account_2['follower']
 guess=int(input("who has more follower type1 or type2 "))
 print(follower_count1)
 print(follower_count2)

 is_correct=check_correct(follower_count1,follower_count2,guess)#true or 1
 os.system('cls')
 if(is_correct==True):#1==true
    score+=1
    print(f"you are right and your score is{score}")
 else:
   print(f"you are wrong  and your  final score is {score}")
   flag=False