# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        try:
            number = int(input(f"Введите координату по {xy[i]}: "))
            a.append(number)
        except ValueError:
            print("Ты ошибся. Вводить надо целые числа!")
    return a


def calc_leng(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки A")
pointA = input_numbers(2)
print("Введите координаты точки B")
pointB = input_numbers(2)

print(f"Длина отрезка: {calc_leng(pointA, pointB):.2f}")