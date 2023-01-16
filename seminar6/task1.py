# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_array(size=6):
    list = [random.randint(0,10) for i in range(size)]
    return list

def sum_odd(list: list):
    return sum([num for i,num in enumerate(list) if i%2==0])

list = create_array()
sum = sum_odd(list)
print(f"Список чисел > {list}")
print(f"Сумма > {sum}")