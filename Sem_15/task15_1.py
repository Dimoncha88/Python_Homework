'''
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров. 
'''

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
# строковое представление. Функцию hex используйте для проверки своего результата.

import logging

number = int(input('Введите число: '))
input_number = number

logging.basicConfig(level=logging.INFO, filename="file_task1.log", encoding="utf-8")

logger = logging.getLogger(__name__)

i = 16
# print(hex(number))

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
logger.info(f'Число {input_number} в шестнадцатеричном формате = {res}')
print(res)