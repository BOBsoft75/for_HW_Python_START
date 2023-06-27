# Была выполнена 2 задача из домашнего задания номер 2.

# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


# from fractions import Fraction
import fractions

frac1 = input(
    'Введи первую дробь в формате “a/b”: ')
frac2 = input(
    'Введи вторую дробь в формате “a/b”: ')
# frac1  = "1/3"
# frac2  = "3/5"

divider1, denominator1 = map(int, frac1.split("/"))
divider2, denominator2 = map(int, frac2.split("/"))

str_sum = str(divider1 * denominator2 + divider2 * denominator1) + "/" \
    + str(denominator1 * denominator2)
str_mul = str(divider1 * divider2) + "/" + str(denominator1 * denominator2)

if (divider1 * denominator2 + divider2 * denominator1) == (denominator1 * denominator2):
    print("Сумма введенных дробей = 1")
else:
    print("Сумма введенных дробей = ", str_sum)
if divider1 == 0 or divider2 == 0:
    print("Произведение введенных дробей = 0")
else:
    print("Произведение введенных дробей = ", str_mul)

# print("Сумма введенных дробей = ", str_sum)
# print("Произведение введенных дробей = ", str_mul)

sum_etalon = fractions.Fraction(frac1) + fractions.Fraction(frac2)
mul_etalon = fractions.Fraction(frac1) * fractions.Fraction(frac2)
if sum_etalon == fractions.Fraction(str_sum) and mul_etalon == fractions.Fraction(str_mul):
    print("Fraction-проверка пройдена")
else:
    print("Что-то пошло не так")

# код из лекции, для примера, дополненный
# f1 = fractions.Fraction(1, 3)
# print(f1)   # 1/3
# f2 = fractions.Fraction(3, 5)
# print(f2)   # 3/5
# print(f1 * f2)  # 1/5
# print(f1 + f2)  # 14/15
# print(fractions.Fraction(1, 5) == fractions.Fraction(3, 15))
# True
