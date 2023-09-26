# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
# строковое представление. Функцию hex используйте для проверки своего результата.

number = int(input('Введите число: '))
i = 16
print(hex(number))

res = ''
while number:
    remains = number % i
    if remains == 10:
        remains = 'A'
    elif remains == 11:
        remains = 'B'
    elif remains == 12:
        remains = 'C'
    elif remains == 13:
        remains = 'D'
    elif remains == 14:
        remains = 'E'
    elif remains == 15:
        remains = 'F'

    res = str(remains) + res
    number //= i
print(res)