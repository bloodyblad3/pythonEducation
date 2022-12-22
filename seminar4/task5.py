# Задача №33: Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def create_polynomial(ratio):
    list = [random.randint(0, 101) for i in range(ratio+1)]
    return list

def create_str(polynomial):
    list = polynomial[::-1]
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

def write_file(filename, polynomial):
    with open(filename, "w") as file:
        file.write(polynomial)

def get_power_polynomial(power):
    if 'x^' in power:
        i = power.find('^')
        num = int(power[i+1:])
    elif ('x' in power) and ('^' not in power):
        num = 1
    else:
        num = -1
    return num

def get_ratio_polynomial(ratio):
    if 'x' in ratio:
        i = ratio.find('x')
        num = int(ratio[:i])
    return num

def calculate_polynomial(polynomial):
    polynomial = polynomial[0].replace(' ', '').split('=')
    polynomial = polynomial[0].split('+')
    list = []
    l = len(polynomial)
    if get_power_polynomial(polynomial[-1]) == -1:
        list.append(int(polynomial[-1]))
        l -= 1
    power = 1
    index = l-1
    while index >= 0:
        if get_power_polynomial(polynomial[index]) != -1 and get_power_polynomial(polynomial[index]) == power:
            list.append(get_ratio_polynomial(polynomial[index]))
            index -= 1
            power += 1
        else:
            list.append(0)
            power += 1
        
    return list

power1 = input_number("Введите натуральную степень для первого файла k = ")
power2 = input_number("Введите натуральную степень для второго файла k = ")
polynomial1 = create_polynomial(power1)
polynomial2 = create_polynomial(power2)
print(f"Первый многочлен > {polynomial1}\nВторой многочлен > {polynomial2}")

write_file("polynomial1.txt", create_str(polynomial1))
write_file("polynomial2.txt", create_str(polynomial2))

with open("polynomial1.txt", "r") as file:
    polynomial1 = file.readlines()
with open("polynomial2.txt", "r") as file:
    polynomial2 = file.readlines()
list1 = calculate_polynomial(polynomial1)
list2 = calculate_polynomial(polynomial2)

size = len(list1)
if size > len(list2):
    size = len(list2)
new_list = [list1[i] + list2[i] for i in range(size)]

if len(list1) > len(list2):
    size2 = len(list1)
    for i in range(size, size2):
        new_list.append(list1[i])
else:
    size2 = len(list2)
    for i in range(size, size2):
        new_list.append(list2[i])
write_file("result.txt", create_str(new_list))

with open("result.txt", "r") as file:
    result_polynomial = file.readlines()
print(f"Результат > {result_polynomial}")