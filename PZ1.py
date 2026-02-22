#Вариант 3

a, b, c = 2, 1, 0.5
for x in range(-3, 4, 1):
    if x == 0:
        F = a + b
    elif x > 0:
        F = (a * x) / (b + c)
    else:
        F = c * (x ^ 2) - a
    print(f'При х = {x}, F(x) = {F}')


