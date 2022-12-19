# Задача №23: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]
import random

def create_array(size=6):
    list = [random.randint(0,10) for i in range(size)]
    return list

def mult_pairs(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    return new_list

list = create_array(5)
print(f"Сгенерированный список > {list}\nПроизведения пар > {mult_pairs(list)}")