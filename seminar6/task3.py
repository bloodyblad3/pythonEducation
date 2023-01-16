# Задача №23: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]

import random 

def create_array(size=5):
    list = [random.randint(0,10) for i in range(size)]
    return list

def mult_pairs(list):
    return [list[i] * list[-i-1] for i in range(len(list)//2 + len(list)%2)]

list = create_array()
pairs = mult_pairs(list)
print(f"Список > {list}")
print(f"Произведение > {pairs}")