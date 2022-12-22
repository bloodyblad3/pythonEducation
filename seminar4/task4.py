# Задача №33: Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def write_file(polynomial):
    with open("polynomial.txt", "w") as file:
        file.write(polynomial)

def create_polynomial(ratio):
    list = [random.randint(0, 101) for i in range(ratio+1)]
    return list

def create_str(power):
    list = power[::-1]
    write = ''
    if len(list) < 1:
        write = "x = 0"
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                write += f"{list[i]}x^{len(list)-i-1}"
                if list[i+1] != 0:
                    write += " + "
            elif i == len(list) - 2 and list[i] != 0:
                write += f"{list[i]}x"
                if list[i+1] != 0:
                    write += " + "
            elif i == len(list) - 1 and list[i] != 0:
                write += f"{list[i]} = 0"
            elif i == len(list) - 1 and list[i] == 0:
                write += " = 0"
    return write

power = input_number("Введите натуральную степень k = ")
ratio = create_polynomial(power)
write_file(create_str(ratio))