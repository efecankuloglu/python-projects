def board(lt):
    print("-" * 9)
    for i in range(0, 3):
        print(f"| {' '.join(lt[i])} |")
    print("-" * 9)

def win_situs(lt):
    new_lt = []
    [new_lt.extend(i) for i in lt]

    win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    lines = 0
    if abs(new_lt.count("X") - new_lt.count("O")) > 1:
        return "Impossible"
    else:
        for win_state in win_states:
            if new_lt[win_state[0]] == new_lt[win_state[1]] == new_lt[win_state[2]] == "X":
                lines += 1
            elif new_lt[win_state[0]] == new_lt[win_state[1]] == new_lt[win_state[2]] == "O":
                lines += 1
        if lines > 1:
            return "Impossible"
    for win_state in win_states:
        if new_lt[win_state[0]] == new_lt[win_state[1]] == new_lt[win_state[2]] == "X":
            return "X wins"
        elif new_lt[win_state[0]] == new_lt[win_state[1]] == new_lt[win_state[2]] == "O":
            return "O wins"
    if new_lt.count("X") + new_lt.count("O") == 9:
        return "Draw"


# cells = input("Enter cells: ")

lt = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board(lt)

count = 0

while True:
    coor = input("Enter the coordinates: ")
    if not coor.split()[0].isdigit() or not coor.split()[1].isdigit():
        print("You should enter numbers!")
        continue
    else:
        x = int(coor.split()[0]) - 1
        y = int(coor.split()[1]) - 1
        if x > 2 or y > 2:
            print("Coordinates should be from 1 to 3!")
            continue
        elif lt[x][y] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        elif count % 2 == 0:
            lt[x][y] = "X"
            count += 1
            board(lt)
            if win_situs(lt):
                print(win_situs(lt))
                break
            else:
                continue
        elif count % 2 != 0:
            lt[x][y] = "O"
            count += 1
            board(lt)
            if win_situs(lt):
                print(win_situs(lt))
                break
            else:
                continue



