#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def print_list(list):
    for i in list:
        print(i, end=' ')
    print()

size = input_number("Введите вложенность списка: ")
list = [random.randint(0,10) for i in range(size)]
print_list(list)

first_pos = input_number("Введите первую позицию: ")
second_pos = input_number("Введите вторую позицию: ")
print(f"Произведение данных чисел {list[first_pos]}, {list[second_pos]}\n{list[first_pos]*list[second_pos]}")