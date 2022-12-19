# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def range_quarter(num: int):
    if num != 0 and num <5:
        if num == 1:
            print("x и y > 0")
        elif num == 2:
            print("x < 0 и y > 0")
        elif num == 3:
            print("x < 0 и y < 0")
        elif num == 4:
            print("x > 0 и y < 0")
    else:
        print("введите корректную четверть")

quarter = input_number("Введите номер четверти: ")
range_quarter(quarter)