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

num = input_number("Введите число: ")

if num >= 1 and num <= 5:
    print("нет")
elif num < 1 or num > 7:
    print(". _. в неделе ток 7 дней :)")
else:
    print("да")