x = float(input('Введите x:'))
alpha = int(input('Укажите степень:'))
n = 0
summ = 0
proizv = 1
next_part = 1
eps = 0.0001

while abs(next_part) > eps:
    for k in range(1, n + 1):
        proizv *= (alpha - k + 1) / k
    next_part *= proizv * pow(x, n) + 1
    summ += next_part
    proizv = 1
    n += 1
print(f'При достижении точности {eps}, степени: {alpha}, текущий член суммы = {round(next_part,5)} при сумме: {round(summ,5)}')

