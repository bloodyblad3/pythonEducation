# Создайте программу для игры в ""Крестики-нолики"".

area = []
turn = 0

def get_number(string: str, min_num:int = None, max_num:int = None) -> int:
    while True:
        try:
            num = int(input(string))
            if min_num and num < min_num:
                raise ValueError
            elif max_num and num > max_num:
                raise ValueError
            return num
        except ValueError:
            print("Неправильный ввод")

def show_gameboard(area):
    for line in area:
        print(line)

def start_game():
    global area, turn
    area = [
        ['*','*','*'],
        ['*','*','*'],
        ['*','*','*']
    ]
    turn = 0

def chek_win(symb: str) -> bool:
    global area
    for i, line in enumerate(area):
        vertical = [area[i][i], area[i-1][i], area[i-2][i]]
        if all(map(lambda char: char == symb, line)):
            return True
        elif all(map(lambda char: char == symb, vertical)):
            return True
    horizontal = [area[0][0], area[1][1], area[2][2]]
    horizontal2 = [area[2][2], area[1][1], area[2][0]]
    if (len(set(horizontal)) == 1 and '*' not in horizontal) or (len(set(horizontal2)) == 1 and '*' not in horizontal2):
        return True
    return False

def game():
    global area, turn
    player = turn % 2 + 1
    print(f"Ход игрока №{player}")
    show_gameboard(area)
    row = get_number("Введите номер строки (1,2,3): ", min_num=1, max_num=3)
    column = get_number("Введите номер столбца(1,2,3): ", min_num=1, max_num=3)
    if area[row-1][column-1] != '*':
        print("Эта клетка уже занята..")
    char = 'x' if player == 1 else '0'
    area[row-1][column-1] = char
    if chek_win(char):
        show_gameboard(area)
        print(f"Победил игрок №{player}, который играл за {char}")
        return 1
    turn += 1
    if turn == 9:
        print("Выиграла дружба")
        return -1
    return game()

while True:
    print("Игра крестики нолики")
    start_game()
    game()
    choice = input("Хотите сыграть еще?\nда/нет\n").lower()
    if choice == "да":
        continue
    break
