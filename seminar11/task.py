from sympy import *
from sympy.plotting import plot

# Определить корни
x = Symbol('x')
func = -5*x**2 + 10*x - 150
x1, x2 = solve(func)
print(x1, x2)

# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
print(solve(diff(func) > 0))
print(solve(diff(func) < 0))

# Построить график
func_plot = plot(func)

# Вычислить вершину
top = solve(diff(func))[0]
print(top)

# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0
print(solve(func > 0))
print(solve(func < 0))