# Была выполнена 3 задача из домашнего задания номер 1.

"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

import random


MIN_VALUE = 0
MAX_VALUE = 1000
TRY_COUNT = 10


number = random.randint(MIN_VALUE, MAX_VALUE)
trying_now = 0
user_number = 0

print("Загаданно целое число от 0 до 1000. Угадайте с 10 попыток!")
while trying_now < TRY_COUNT:
    user_number = int(input(
        f"Введите целое число от {MIN_VALUE} до {MAX_VALUE} включительно: "))

    if user_number not in range(MIN_VALUE, MAX_VALUE+1):
        print("Число вне допустимого диапазона (0-1000)")
        continue
    if user_number == number:
        print("Вы угадали!")
        break
    elif user_number < number:
        print(
            f"Попытка {trying_now + 1}. Загаданное число больше")
    else:
        print(
            f"Попытка {trying_now + 1}. Загаданное число меньше")
    trying_now += 1
else:
    print("Попытки закончились, Вы проиграли!")
