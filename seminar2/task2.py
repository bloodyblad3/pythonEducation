# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def mult(n: int):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = input_number("Введите число: ")

list = []
for i in range(1, num + 1):
    list.append(mult(i))
print(f"Произведения чисел от 1 до {num}: {list}")