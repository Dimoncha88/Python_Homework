# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1001)
count = 10

while count > 0:
    num_input = int(input('Угадайте загаданное число: '))
    if num_input == num:
        print('Жена МОЛОДЕЦ')
        break
    elif num_input > num:
        print('Меньше')
        count -=1
    else:
        print('Больше')
        count -=1
    print('Осталось попыток', count)
if count == 0:
    print('Вы исчерпали попытки, загаданное число', num)