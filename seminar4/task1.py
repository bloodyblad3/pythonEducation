# Задача №30: Вычислить число c заданной точностью d. Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from math import pi

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

# Пример ввода:
# Введите число для заданной точности числа π: 4
# Вывод: 3.1416
d =  input_number("Введите число для заданной точности числа π: ")
print(f'число π с заданной точностью {d} равно {round(pi, d)}')