# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# # - 2 -> 10

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def to_binary(num: int):
    s = ""
    while num != 0:
        s = str(num%2) + s
        num //= 2
    return s

num = input_number("Введите число для преобразования: ")
print(f"Число {num} в двоичном виде > {to_binary(num)}")