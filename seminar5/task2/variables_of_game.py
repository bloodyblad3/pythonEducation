from utils import max_candies
from random import randint, choice
def player(count_of_candies, max_for_step):
    while True:
        candy = max_candies("Введите кол-во конфет которое хотите взять: ", count_of_candies)
        max_for_step = max_for_step if max_for_step < count_of_candies else count_of_candies
        if candy > max_for_step:
            print(f"Нельзя взять больше {max_for_step}")
        else:
            return candy

def bot(count_of_candies, max_for_step):
    candy = randint(1, max_for_step if max_for_step < count_of_candies else count_of_candies)
    print(f"Бот взял {candy}")
    return candy

def ai(count_of_candies, max_for_step):
    if count_of_candies % max_for_step == 0:
        candy = max_for_step - 1
    else:
        candy = count_of_candies%max_for_step
    print(f"ИИ берет {candy}")
    return candy

def game(opponent, count_of_candies, max_for_step):
    player_name = "Игрок"
    opponent_name = "Противник"
    players = ["Победил: ", player_name, opponent_name]
    turn = choice([-1,1])
    while count_of_candies > 0:
        print(f"На столе {count_of_candies} конфет")
        print(f"Ходит {players[turn]}")
        if turn == 1:
            candy = player(count_of_candies, max_for_step)
        else:
            if opponent == "игрок":
                candy = player(count_of_candies, max_for_step)
            elif opponent == "бот":
                candy = bot(count_of_candies, max_for_step)
            else:
                candy = ai(count_of_candies, max_for_step)
        count_of_candies -= candy
        turn *= -1
    players.remove(players[turn])
    print("".join(players))
        

