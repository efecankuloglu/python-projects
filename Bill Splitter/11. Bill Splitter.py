import random

friends_lt = []

print("Enter the number of friends joining (including you):")
friends_number = int(input())

if friends_number < 1:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(friends_number):
        friends_name = input()
        friends_lt.append(friends_name)
    print("\nEnter the total bill value:")
    bill = int(input())
    print("\nDo you want to use the 'Who is lucky?' feature? Write Yes/No:")
    lucky_feat = input()
    if lucky_feat == "Yes":
        lucky_per = random.choice(friends_lt)
        print(f"\n{lucky_per} is the lucky one!\n")
        friends_dict = dict.fromkeys(friends_lt, round((bill / (friends_number - 1)), 2))
        friends_dict[lucky_per] = 0
        print(friends_dict)
    elif lucky_feat == "No":
        print("\nNo one is going to be lucky")
        friends_dict = dict.fromkeys(friends_lt, round((bill / friends_number), 2))
        print(friends_dict)