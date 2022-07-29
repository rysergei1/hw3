from math import sin, factorial, radians

eps = 0.000001
current = 1
sum = 0
n = 0

corner = (float(input("Set the x in radians:")))
rad = radians(corner)
while abs(current) > eps:
    current = pow(-1, n) * (pow(rad, 2 * n + 1)) / factorial(2 * n + 1)
    sum += current
    n += 1
print(f'При достижении точности {eps}, угле: {corner}, текущий член суммы = {current} при сумме: {round(sum,5)}')


