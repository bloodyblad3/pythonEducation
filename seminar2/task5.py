# Реализуйте алгоритм перемешивания списка.
import random

def shuffle_list(list):
    # Создаем копию
    list = list[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_aleatory = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    # Возвращаем список
    return list

list = [random.randint(0,10) for i in range(5)]
print(list)
print(shuffle_list(list))