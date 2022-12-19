# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def create_array(size=6):
    list = [random.randint(0,10) for i in range(size)]
    return list

def sum_not_even(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
        else:
            continue
    return sum

list = create_array()
print(list)
print(sum_not_even(list))