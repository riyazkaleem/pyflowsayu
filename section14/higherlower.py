#importing libraries
import art
import gamedata
import random
import os

#implementation
# print(art.logo)
gamedatacount = len(gamedata.data)
name='name'
description = 'description'
country = 'country'
followers = 'follower_count'
winflag = True
scorecount = 0
# print(f'index1: {randomindex1}, index2: {randomindex2}')
# print(f'data1: {gamedata.data[randomindex1][name]}, data1: {gamedata.data[randomindex1][name]}')
print(art.logo)
randomindex1 = random.randint(0, gamedatacount-1)
randomindex2 = random.randint(0, gamedatacount-1)
print(f'compare A: {gamedata.data[randomindex1][name]}, {gamedata.data[randomindex1][description]} from {gamedata.data[randomindex1][country]}')
print(art.vs)
print(f'compare B: {gamedata.data[randomindex2][name]}, {gamedata.data[randomindex2][description]} from {gamedata.data[randomindex2][country]}')
while(winflag): 
    userinput = input("Who has more followers? Type 'A' or 'B':")
    if userinput == 'A':
        if gamedata.data[randomindex1][followers] > gamedata.data[randomindex2][followers]:
            scorecount+=1
            os.system('cls')
            print(art.logo)
            print(f"You're right! Current score: {scorecount}.")
            print(f'compare A: {gamedata.data[randomindex1][name]}, {gamedata.data[randomindex1][description]} from {gamedata.data[randomindex1][country]}')
            print(art.vs)
            print(f'compare B: {gamedata.data[randomindex2][name]}, {gamedata.data[randomindex2][description]} from {gamedata.data[randomindex2][country]}')
            randomindex1 = randomindex2
            randomindex2 = random.randint(0, gamedatacount-1)
        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {scorecount}")
            winflag = False
    elif userinput == 'B':
        if gamedata.data[randomindex2][followers] > gamedata.data[randomindex1][followers]:
            scorecount+=1
            os.system('cls')
            print(art.logo)
            print(f"You're right! Current score: {scorecount}.")
            print(f'compare A: {gamedata.data[randomindex1][name]}, {gamedata.data[randomindex1][description]} from {gamedata.data[randomindex1][country]}')
            print(art.vs)
            print(f'compare B: {gamedata.data[randomindex2][name]}, {gamedata.data[randomindex2][description]} from {gamedata.data[randomindex2][country]}')
            randomindex1 = randomindex2
            randomindex2 = random.randint(0, gamedatacount-1)
        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {scorecount}")
            winflag = False
        
