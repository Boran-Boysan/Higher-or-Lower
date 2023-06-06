import random
import os
from art import logo
from art import vs
from game_data import data



score = 0
choose = " "
a = random.randint(0,len(data)-1)
A = data[a]
b = random.randint(0,len(data)-1)
B = data[b]
game = "y"

while game == "y":
    print(logo)
    if(score > 0):
        print(f"You are right! Current score: {score}")

    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")

    print(vs)

    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")

    while choose != "a" and choose != "b":
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    print(choose)

    if choose == "a":
        if(A['follower_count'] > B['follower_count']):
            score +=1
            choose = " "
            os.system("cls")
            b = random.randint(0,len(data)-1)
            B = data[b]
        
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game = "n"

    elif choose == "b":
        if(A['follower_count'] < B['follower_count']):
            score +=1
            choose = " "
            os.system("cls")
            a = b
            A = data[a]
            b = random.randint(0,len(data)-1)
            B = data[b]
        
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game = "n"

