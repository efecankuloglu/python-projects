import random

lt = [[i, j] for i in range(7) for j in range(i, 7)]
stock = []
comp = []
player = []
snake = []

while True:
    for _ in range(14):
        el = random.choice(lt)
        stock.append(el)
        lt.remove(el)
    for _ in range(7):
        el = random.choice(lt)
        comp.append(el)
        lt.remove(el)
    for _ in range(7):
        el = random.choice(lt)
        player.append(el)
        lt.remove(el)
    for i in range(6, -1, -1):
        if [i, i] in comp:
            status = "player"
            snake_piece = [i, i]
            snake.append(snake_piece)
            comp.remove(snake_piece)
            break
        elif [i, i] in player:
            status = "computer"
            snake_piece = [i, i]
            snake.append(snake_piece)
            player.remove(snake_piece)
            break
    if status:
        break

while True:
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(comp)}")

    if len(snake) > 6:
        print(f"\n{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}\n")
    else:
        print(f"\n{''.join([str(i) for i in snake])}\n")
    print("Your pieces:")
    for i in range(1, len(player) + 1):
        print(f"{i}:{player[i - 1]}")

    if len(player) == 0:
        print("\nStatus: The game is over. You won!")
        break
    elif len(comp) == 0:
        print("\nStatus: The game is over. The computer won!")
        break
    elif len(stock) == 0:
        print("\nStatus: The game is over. It's a draw!")
        break
    for i in range(7):
        if sum([x.count(i) for x in snake]) == 8 and snake[0][0] == i and snake[-1][1] == i:
            print("Status: The game is over. It's a draw!")
            break
        break

    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        command = input()

        count = {0: sum([i.count(0) for i in comp]) + sum([i.count(0) for i in snake]),
                 1: sum([i.count(1) for i in comp]) + sum([i.count(1) for i in snake]),
                 2: sum([i.count(2) for i in comp]) + sum([i.count(2) for i in snake]),
                 3: sum([i.count(3) for i in comp]) + sum([i.count(3) for i in snake]),
                 4: sum([i.count(4) for i in comp]) + sum([i.count(4) for i in snake]),
                 5: sum([i.count(5) for i in comp]) + sum([i.count(5) for i in snake]),
                 6: sum([i.count(6) for i in comp]) + sum([i.count(6) for i in snake])}

        comp.sort(key=lambda x: count[x[0]] + count[x[1]], reverse=True)
        for i in comp:
            if i[0] == snake[-1][1]:
                snake.append(i)
                comp.remove(i)
                break
            elif i[1] == snake[-1][1]:
                snake.append(i[::-1])
                comp.remove(i)
                break
            elif i[0] == snake[0][0]:
                snake.insert(0, i[::-1])
                comp.remove(i)
                break
            elif i[1] == snake[0][0]:
                snake.insert(0, i)
                comp.remove(i)
                break
        else:
            piece = random.choice(stock)
            comp.append(piece)
            stock.remove(piece)
        status = "player"

    elif status == "player":
        print("\nStatus: It's your turn to make a move. Enter your command.")
        while True:
            command = input()
            if command in [str(i) for i in range(-len(player), len(player) + 1)]:
                if int(command) < 0:
                    piece = player[abs(int(command)) - 1]
                    if snake[0][0] == piece[1]:
                        snake.insert(0, piece)
                        player.remove(piece)
                        break
                    elif snake[0][0] == piece[0]:
                        snake.insert(0, piece[::-1])
                        player.remove(piece)
                        break
                    else:
                        print("Illegal move. Please try again.")
                        continue
                elif int(command) == 0:
                    piece = random.choice(stock)
                    player.append(piece)
                    stock.remove(piece)
                    break
                elif int(command) > 0:
                    piece = player[int(command) - 1]
                    if snake[-1][1] == piece[0]:
                        snake.append(piece)
                        player.remove(piece)
                        break
                    elif snake[-1][1] == piece[1]:
                        snake.append(piece[::-1])
                        player.remove(piece)
                        break
                    else:
                        print("Illegal move. Please try again.")
                        continue
            elif command not in [str(i) for i in range(-len(player), len(player))]:
                print("Invalid input. Please try again.")
            else:
                print("Invalid input. Please enter a number.")
                continue
        status = "computer"
