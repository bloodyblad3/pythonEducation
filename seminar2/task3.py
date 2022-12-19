#  Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#  Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("это не число!")
    return number
   
num = input_number("Введите число: ")
list = [round((1 + 1 / i)**i, 2) for i in range(1, num + 1)]
print(f"Последовательность: {list}\n Сумма: {round(sum(list), 2)}")