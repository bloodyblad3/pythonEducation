# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number


def check_weekend(num: int):
    if num == 6 or num == 7:
        print("да")
    elif num > 0 and num < 6:
        print("да")
    else:
        print(". _. в неделе ток 7 дней :)")

num = input_number("Введите число: ")
check_weekend(num)