# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number

def prime_factors(num: int) -> list:
    list = []
    i = 2
    while i <= num:
        if num % i == 0:
            list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return list

num = input_number("Введите число: ")
factors = prime_factors(num)
print(f"Простые множители числа {num} > {factors}")