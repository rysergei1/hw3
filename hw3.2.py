from math import cos, radians, factorial

x= float(input('Введите значение в радианах:'))
x_rad = radians(x)
n = 0
next_part = 1
summ = 0
eps = 0.00001
print(x_rad)

while abs(next_part) > eps:
    next_part = pow(-1, n) * pow (x_rad, 2 * n) / factorial(2 * n)
    summ += next_part
    n += 1
print(f'При достижении точности {eps}, угле: {x}, текущий член суммы = {next_part} при сумме: {round(summ,5)}')




