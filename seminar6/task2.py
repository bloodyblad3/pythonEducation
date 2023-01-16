# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def count_distance():
    point_a = [int(input(f"Введите {i} точки A: ")) for i in 'xy']
    point_b = [int(input(f"Введите {i} точки B: ")) for i in 'xy'] 
    return sum((point[0] - point[1])**2 for point in zip(point_a, point_b))**0.5

sum = count_distance()
print(f"{sum:.2f}")