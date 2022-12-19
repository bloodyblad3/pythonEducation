# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def input_number(text: str) -> int:
    try:
        number = float(input(text))
    except ValueError:
        print("это не число!")
    return number

def sum_num(num: int):
    sum = 0
    for i in str(num):
        if i != '.':
            sum += int(i)
    return sum

num = input_number("Введите вещественное число: ")
print(f"Сумма чисел -> {sum_num(num)}")