from utils import input_number, max_candies
from variables_of_game import game

count_of_candies = input_number("Введите кол-во конфет на столе: ") 
max_for_step = max_candies("Макс. кол-во которое можно взять за ход: ", count_of_candies)

while True:
    variable_of_games = input_number('''
                            Выберите режим игры:
                            1 - игрок против игрока
                            2 - игрок против бота
                            3 - игрок против ИИ
                            4 - выход из игры
                            ''')
    if variable_of_games < 1 or variable_of_games > 4:
        print("Такого режима не существует...")
    elif variable_of_games == 1:
        game("игрок", count_of_candies, max_for_step)
    elif variable_of_games == 2:
        game("бот", count_of_candies, max_for_step)
    elif variable_of_games == 3:
        game("ИИ", count_of_candies, max_for_step)
    else:
        print("Пока!")
        break
    input()