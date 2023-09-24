# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

a1 = int(input('Введите числитель первой дроби: '))
b1 = int(input('Введите знаменатель первой дроби: '))
a2 = int(input('Введите числитель второй дроби: '))
b2 = int(input('Введите знаменатель второй дроби: '))

res_sum = 0
res_multi = 0
frac1 = fractions.Fraction(a1, b1)
frac2 = fractions.Fraction(a2, b2)
print(f'Введенные дроби: {frac1} {frac2}')
print(f'Сумма = {frac1 + frac2}')
print(f'Произведение = {frac1 * frac2}')
print()

res_multi = f'{(a1 * a2)}/{(b1 * b2)}'
for i in range(2,10):
    if (a1 * a2) % i == 0 and (b1 * b2) % i == 0:
        res_multi = f'{int((a1 * a2)/i)}/{int((b1 * b2)/i)}'
        if a1 * a2 == b1 * b2:
            res_multi = 1

if b1 % b2 == 0:
    frac = b1
    a2 = (b1 / b2) * a2
elif b2 % b1 == 0:
    frac = b2
    a1 = (b2 / b1) * a1
else:
    frac = b1 * b2
    a1 *= b2
    a2 *= b1
res_sum = f'{int(a1 + a2)}/{frac}'
for i in range(2,10):
    if (a1 + a2) % i == 0 and frac % i == 0:
        res_sum = f'{int((a1 + a2)/i)}/{int(frac/i)}'
        if a1 + a2 == frac:
            res_sum = 1

print(f'Сумма = {res_sum}')
print(f'Произведение = {res_multi}')
