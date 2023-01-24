# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def fib(num: int):
    lst = [0]
    for i in range(0,num+1):
        if i==1:
            lst.append(1)
            lst.insert(0, 1)
        elif i==2:
            lst.append(1)
            lst.insert(0, -1)
        elif i>2:
            lst.append(lst[-1]+lst[-2])
            lst.insert(0, -lst[-1] if i%2 == 0 else lst[-1])
    return lst

num = input_number("Введите число: ")
print(fib(num))  