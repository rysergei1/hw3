eps = 0.001
x = int(input())
summ = 0
n = 1
next_part = 1
while abs(next_part) > eps:
    next_part = pow(-1, n + 1) * (pow(x, n) / n)
    summ += next_part
n += 1
print(f'При достижении точности {eps}, значении: {x}, текущий член суммы = {next_part} при сумме: {round(summ,5)}')