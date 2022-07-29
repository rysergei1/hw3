from math import factorial
x = int(input('Введите значение'))
n = 1
eps = 0.001
summ = 0
next_part = 1
while abs(next_part) > eps:
    next_part = pow(x, n) / factorial(n)
    summ += next_part
    n += 1
print(f'При достижении точности {eps}, значении: {x}, текущий член суммы = {next_part} при сумме: {round(summ,5)}')