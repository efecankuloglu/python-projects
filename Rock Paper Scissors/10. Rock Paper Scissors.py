import random
import os

win_cond = {
    "rock": ["scissors", "lizard", "fire", "snake", "human", "tree", "wolf", "sponge"],
    "paper": ["rock", "spock", "air", "water", "dragon", "devil", "lightning", "gun"],
    "scissors": ["paper", "lizard", "snake", "human", "tree", "wolf", "sponge", "air"],
    "spock": ["scissors", "rock"],
    "lizard": ["paper", "spock"],
    "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
    "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
    "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
    "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
    "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
    "air": ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"],
    "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
    "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
    "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
    "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
    "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"],
    "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"]}

score = {}

p_name = input("Enter your name: ")
print(f"Hello, {p_name}")
if os.path.isfile("rating.txt"):
    with open("rating.txt", "r") as rating_file:
        for i in rating_file:
            record = i.split()
            if record[0] == p_name:
                score[p_name] = score.get(p_name, 0) + int(record[1])

opt_1 = ["rock", "paper", "scissors"]
opt_2 = ["rock", "paper", "scissors", "spock", "lizard"]
opt_3 = ["rock", "paper", "scissors", "fire", "snake", "human", "tree", "wolf", "sponge", "air", "water", "dragon", "devil", "lightning", "gun"]

while True:
    game_opt = input(f"""
Please select game option: 
1 - {", ".join(opt_1)} 
2 - {", ".join(opt_2)}
3 - {", ".join(opt_3)}
""")
    if game_opt == "1":
        opt_list = opt_1
        break
    elif game_opt == "2":
        opt_list = opt_2
        break
    elif game_opt == "3":
        opt_list = opt_3
        break
    else:
        print("Invalid Input")
        continue
    
print("Okay, let's start")

while True:
    p_choice = input("Please enter one of option or !rating for score or !exit for quit.\n")
    if p_choice == "!exit":
        print("Bye!")
        break
    elif p_choice == "!rating":
        print(f"Your rating: {score[p_name]}")
        continue
    elif p_choice not in ["!exit", "!rating"] and p_choice not in opt_list:
        print("Invalid input")
        continue
    comp = random.choice(opt_list)

    if p_choice == comp:
        print(f"There is a draw ({p_choice})")
        score[p_name] = score.get(p_name, 0) + 50
    elif comp in win_cond[p_choice]:
        print(f"Well done. The computer chose {comp} and failed")
        score[p_name] = score.get(p_name, 0) + 100
    elif comp not in win_cond[p_choice]:
        print(f"Sorry, but the computer chose {comp}")
