# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import random

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def create_array(size=10):
    list = [f"{random.randint(0,10)}" for i in range(size)]
    return list

def find_num(num_list, search_num: int) -> bool:
    return True if [elem for elem in num_list if str(search_num) == elem] else False

list = create_array()
bool = find_num(list, input_number("Введите число, чтобы проверить есть ли оно в списке: "))
print(list)
print(bool)