# Задача №24: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

def create_array(size=6):
    list = [round(random.uniform(-10.99,10), 2) for i in range(size)]
    return list

list = create_array()
diff = [round(i%1,2) for i in list if i%1 != 0]
print(list)
print(round(max(diff) - min(diff), 2))
