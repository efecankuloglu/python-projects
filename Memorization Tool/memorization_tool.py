from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")

Base = declarative_base()


class Table(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


menu_1 = ["Add flashcards", "Practice flashcards", "Exit"]
menu_2 = ["Add a new flashcard", "Exit"]

flashcard_dt = {}

while True:

    for i, j in enumerate(menu_1):
        print(f"{i + 1}. {j}")
    menu_1_choice = input()
    if menu_1_choice == "1":
        while True:
            print("")
            for x, y in enumerate(menu_2):
                print(f"{x + 1}. {y}")
            menu_2_choice = input()
            if menu_2_choice == "1":
                while True:
                    quest = input("\nQuestion:")
                    if quest:
                        while True:
                            ans = input("Answer:")
                            if not ans:
                                continue
                            else:
                                break
                    else:
                        continue
                    new_data = Table(question=quest, answer=ans, box=1)
                    session.add(new_data)
                    session.commit()
                    break
            elif menu_2_choice == "2":
                print("")
                break
            else:
                print(f"{menu_2_choice} is not an option")
                continue

    elif menu_1_choice == "2":
        if session.query(Table).all():
            result_list = session.query(Table).all()
            for i in range(len(result_list)):
                print(f'\nQuestion: {result_list[i].question}:\npress "y" to see the answer:\n'
                      f'press "n" to skip:\npress "u" to update:')
                ans_input = input()
                if ans_input == "y":
                    print(f"\nAnswer: {result_list[i].answer}")
                    print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
                    y_answer_menu = input()
                    if y_answer_menu == "y":
                        result_list[i].box += 1
                        if result_list[i].box == 3:
                            session.delete(result_list[i])
                            session.commit()
                    elif y_answer_menu == "n":
                        print("")
                        continue
                    else:
                        print(f"{y_answer_menu} is not an option")
                        continue
                elif ans_input == "n":
                    print('press "y" if your answer is correct:\npress "n" if your answer is wrong:')
                    n_answer_menu = input()
                    if n_answer_menu == "y":
                        result_list[i].box += 1
                        if result_list[i].box == 3:
                            session.delete(result_list[i])
                            session.commit()
                        continue
                    elif n_answer_menu == "n":
                        print("")
                        continue
                    else:
                        print(f"{n_answer_menu} is not an option")
                        continue
                elif ans_input == "u":
                    print('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')
                    edit_input = input()
                    if edit_input == "e":
                        print(f"current question: {result_list[i].question}")
                        new_quest = input("please write a new question:\n")
                        result_list[i].question = new_quest
                        print(f"current answer: {result_list[i].answer}")
                        new_ans = input("please write a new answer:\n")
                        result_list[i].answer = new_ans
                        session.commit()
                    elif edit_input == "d":
                        session.delete(result_list[i])
                        session.commit()
                    else:
                        print(f"{edit_input} is not an option")
                        continue
                else:
                    print(f"{ans_input} is not an option")
                    continue
        else:
            print("\nThere is no flashcard to practice!\n")
            continue

    elif menu_1_choice == "3":
        print("Bye!")
        break

    else:
        print(f"{menu_1_choice} is not an option")
        continue
