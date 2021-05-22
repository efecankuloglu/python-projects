import random

levels = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}

print(f"""Which level do you want? Enter a number:
1 - {levels[1]}
2 - {levels[2]}""")

while True:
    try:
        level = int(input())
        if level == 1:
            count = 0
            for i in range(5):
                nr1 = random.randint(2, 9)
                nr2 = random.randint(2, 9)
                operation = random.choice(["+", "-", "*"])

                print(f'{nr1} {operation} {nr2}')

                if operation == "+":
                    sol = nr1 + nr2

                elif operation == "-":
                    sol = nr1 - nr2

                elif operation == "*":
                    sol = nr1 * nr2

                while True:
                    try:
                        answer = int(input())
                        if answer == sol:
                            print("Right!")
                            count += 1
                        else:
                            print("Wrong!")
                        break
                    except:
                        print("Wrong format! Try again.")
        elif level == 2:
            count = 0
            for i in range(5):
                nr = random.randint(11, 29)
                print(f'{nr}')
                sol = nr ** 2
                while True:
                    try:
                        answer = int(input())
                        if answer == sol:
                            print("Right!")
                            count += 1
                        else:
                            print("Wrong!")
                        break
                    except:
                        print("Wrong format! Try again.")
        else:
            print("Incorrect format.")
            continue
    except ValueError:
        print("Incorrect format.")
    print(f"Your mark is {count}/5. Would you like to save the result? Enter yes or no.")
    save_input = input()
    if save_input.lower() == "yes" or save_input.lower() == "y":
        name = input("What is your name?")
        with open("results.txt", "a+") as f:
            f.write(f"{name}: {count}/5 in level {level} ({levels[level]}).")
        print('The results are saved in "results.txt"')
        break
    else:
        break
