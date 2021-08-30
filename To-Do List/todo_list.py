from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///todo.db?check_same_thread=False")

Base = declarative_base()


class Table(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default="default_value")
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# rows = session.query(Table).all() # Selecting all rows from the table_name
# first_row = rows[0] # In case rows list is not empty

# print(first_row.string_field) # Will print the value of the string_field
# print(first_row.id) # Will print the id of the row
# print(first_row) # Will print the string that was returned by the __repr__ method


def menu():
    options = {1: "Today's tasks", 2: "Week's tasks", 3: "All tasks", 4: "Missed tasks", 5: "Add task",
               6: "Delete task", 0: "Exit"}
    for j in options.keys():
        print(f"{j}) {options[j]}")


while True:
    menu()
    opt_choice = input()
    if opt_choice == "1":
        print(f"\nToday {datetime.today().strftime('%d %b')}:")
        rows = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
        if rows:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task}")
            print("")
        else:
            print("Nothing to do!\n")
        continue

    elif opt_choice == "2":
        for i in range(7):
            day = datetime.today().date() + timedelta(days=i)
            print(f"{day.strftime('%A %d %b')}:")
            rows = session.query(Table).filter(Table.deadline == day).all()
            if rows:
                for j in range(len(rows)):
                    print(f"{j + 1}. {rows[j].task}")
                print("\n")
            else:
                print("Nothing to do!\n")
        continue

    elif opt_choice == "3":
        rows = session.query(Table).order_by(Table.deadline).all()
        print("\nAll tasks:")
        if rows:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task}. {rows[i].deadline.strftime('%#d %b')}")
            print("")
        else:
            print("Nothing to do!\n")
        continue

    elif opt_choice == "4":
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
        print("\nMissed tasks:")
        if rows:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task}. {rows[i].deadline.strftime('%#d %b')}")
            print("")
        else:
            print("Nothing is missed!\n")
        continue

    elif opt_choice == "5":
        text_input = input("\nEnter task")
        year_input, month_input, day_input = map(int, input("Enter deadline").split("-"))
        new_row = Table(task=f"{text_input}",
                        deadline=datetime(year_input, month_input, day_input))
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")
        continue

    elif opt_choice == "6":
        rows = session.query(Table).order_by(Table.deadline).all()
        print("\nChoose the number of the task you want to delete:")
        if rows:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i].task}. {rows[i].deadline.strftime('%#d %b')}")
            delete_number = int(input())
            deleting_row = rows[delete_number - 1]
            session.delete(deleting_row)
            session.commit()
            print("The task has been deleted!")
        else:
            print("Nothing to delete!\n")
        continue

    elif opt_choice == "0":
        print("\nBye!")
        break
