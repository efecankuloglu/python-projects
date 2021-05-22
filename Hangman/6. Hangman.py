import random
import string
print("H A N G M A N")
game = input('Type "play" to play the game, "exit" to quit: ')
if game == "play":
    words = ['python', 'java', 'kotlin', 'javascript']

    chosen = random.choice(words)

    word = ["-" for i in chosen]
    lives = 8
    guessed = []

    while lives > 0:
        print("\n" + "".join(word))
        if lives != 0 and "-" not in word:
            print(f"You guessed the word {''.join(word)}!\nYou survived!")
            break
        letter = input("Input a letter: ")
        guessed.append(letter)
        if len(letter) == 1 and (letter.lower() != letter or not letter.isalpha()):
            print("Please enter a lowercase English letter")
            continue
        elif len(letter) != 1:
            print("You should input a single letter")
            continue
        elif guessed.count(letter) > 1 and (letter not in word or letter in word):
            print("You've already guessed this letter")
            continue
        else:
            if letter in chosen:
                if letter in word:
                    print("No improvements")
                    lives -= 1
                    if lives == 0 and "-" in word:
                        print("You lost!")
                        break
                else:
                    for i in range(len(chosen)):
                        if chosen[i] == letter:
                            word[i] = letter
            elif letter not in chosen:
                lives -= 1
                print("That letter doesn't appear in the word")
                if lives == 0 and "-" in word:
                    print("You lost!")
                    break
else:
    quit()
