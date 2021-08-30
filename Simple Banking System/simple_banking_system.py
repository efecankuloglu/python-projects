import random
import sqlite3

acc_dict = {}


conn = sqlite3.connect("card.s3db")
cur = conn.cursor()

sql_query = """CREATE TABLE IF NOT EXISTS card (
id INTEGER,
number TEXT,
pin TEXT,
balance INTEGER DEFAULT 0
);
"""

cur.execute(sql_query)

conn.commit()


def account_creation():
    original_card_no = f"400000{''.join([str(random.randint(0, 9)) for _ in range(9)])}"

    card_no_lt = [int(original_card_no[i]) * 2 if i % 2 == 0 else int(original_card_no[i]) for i in range(len(original_card_no))]
    valid_card_no = [i - 9 if i > 9 else i for i in card_no_lt]

    if sum(valid_card_no) % 10 == 0:
        original_card_no += str(0)
    else:
        original_card_no += str(10 - (sum(valid_card_no) % 10))

    password = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    acc_dict[original_card_no] = password
    return original_card_no, password


def card_check(card_no):
    card_no_lt = [int(card_no[i]) * 2 if i % 2 == 0 else int(card_no[i]) for i in range(len(card_no[:15]))]
    valid_card_no = [i - 9 if i > 9 else i for i in card_no_lt]
    return (sum(valid_card_no) + int(card_no[15])) % 10 == 0


def sql_insert(card, pin):
    cur.execute(f"INSERT INTO card (number, pin) VALUES ({card}, {pin})")
    conn.commit()


def bank():
    while True:
        options = {1: "Create an account", 2: "Log into account", 0: "Exit"}
        for j in options.keys():
            print(f"{j}. {options[j]}")

        first_opt = int(input())
        if first_opt == 1:
            acc, pw = account_creation()
            print(f"""
Your card has been created
Your card number:
{acc}
Your card PIN:
{pw}\n""")
            sql_insert(acc, pw)
        elif first_opt == 2:
            card_input = input("\nEnter your card number:\n")
            pin_input = input("Enter your PIN:\n")
            if card_input in acc_dict.keys() and pin_input == acc_dict[card_input]:
                print("\nYou have successfully logged in!\n")
            else:
                print("\nWrong card number or PIN!\n")
                continue

            while True:
                login_opt = {1: "Balance", 2: "Add income", 3: "Do transfer", 4: "Close account", 5: "Log out", 0: "Exit"}
                for k in login_opt.keys():
                    print(f"{k}. {login_opt[k]}")

                login_input = int(input())
                if login_input == 1:
                    result = cur.execute(f"SELECT balance FROM card WHERE number = {card_input};")
                    balance = result.fetchone()[0]
                    print(f"\nBalance: {balance}\n")
                    continue
                elif login_input == 2:
                    income = int(input("\nEnter income:\n"))
                    result = cur.execute(f"SELECT balance FROM card WHERE number = {card_input};")
                    balance = result.fetchone()[0] + income
                    cur.execute(f"UPDATE card SET balance = {balance} WHERE number = {card_input};")
                    conn.commit()
                    print("Income was added!\n")
                    continue
                elif login_input == 3:
                    receiving_card = input("\nTransfer\nEnter card number:\n")
                    if card_check(receiving_card):
                        card_results = cur.execute(f"SELECT number FROM card;")
                        card_numbers = card_results.fetchall()
                        card_numbers_lt = [i[0] for i in card_numbers]
                        if receiving_card == login_input:
                            print("You can't transfer money to the same account!")
                            continue
                        elif receiving_card not in card_numbers_lt:
                            print("Such a card does not exist.\n")
                            continue
                        else:
                            send_money = int(input("Enter how much money you want to transfer:\n"))
                            result = cur.execute(f"SELECT balance FROM card WHERE number = {card_input};")
                            balance = result.fetchone()[0]
                            if send_money > balance:
                                print("Not enough money!\n")
                                continue
                            else:
                                balance -= send_money
                                cur.execute(f"UPDATE card SET balance = {balance} WHERE number = {card_input};")
                                result_receiving = cur.execute(f"SELECT balance FROM card WHERE number = {receiving_card};")
                                balance_receiving = result_receiving.fetchone()[0] + + send_money
                                cur.execute(f"UPDATE card SET balance = {balance} WHERE number = {receiving_card};")
                                conn.commit()
                                print("Success\n")
                                continue
                    else:
                        print("Probably you made a mistake in the card number. Please try again!\n")
                        continue

                elif login_input == 4:
                    cur.execute(f"DELETE FROM card WHERE number = {card_input};")
                    print("\nThe account has been closed!\n")
                    conn.commit()
                    break

                elif login_input == 5:
                    print("\nYou have successfully logged out!\n")
                    break
                elif login_input == 0:
                    quit()

        elif first_opt == 0:
            print("\nBye!\n")
            quit()


bank()
