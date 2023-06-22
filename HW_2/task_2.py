# Была выполнена 2 задача из домашнего задания номер 2.

# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.   


# from fractions import Fraction
import fractions

frac1  = input('Введи первую дробь в формате “a/b”: ')
frac2  = input('Введи вторую дробь в формате “a/b”: ')
# frac1  = "1/3"
# frac2  = "3/5"

divider1 = int(frac1[:frac1.find("/")])
denominator1 = int(frac1[frac1.find("/")+1:])
divider2 = int(frac2[:frac2.find("/")])
denominator2 = int(frac2[frac2.find("/")+1:])

str_sum = str(divider1 * denominator2 + divider2 * denominator1) + "/" \
        + str(denominator1 * denominator2)
str_mul = str(divider1 * divider2) + "/" + str(denominator1 * denominator2)
print("Сумма введенных дробей = ", str_sum)
print("Произведение введенных дробей = ", str_mul)

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
