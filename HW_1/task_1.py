# Была выполнена 1 задача их домашнего задания номер 1.

"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним. 
"""

SIDE_A = 2
SIDE_B = 2
SIDE_C = 2

if SIDE_A >= (SIDE_B + SIDE_C):
    print("Сторона треугольника равная " + str(SIDE_A) + ", должна быть меньше суммы длин других сторон (" +
          str(SIDE_B + SIDE_C) + ") - такого треугольника не существует")
elif SIDE_B >= (SIDE_A + SIDE_C):
    print("Сторона треугольника равная " + str(SIDE_B) + ", должна быть меньше суммы длин других сторон (" +
          str(SIDE_A + SIDE_C) + ") - такого треугольника не существует")
elif SIDE_C >= (SIDE_A + SIDE_B):
    print("Сторона треугольника равная " + str(SIDE_C) + ", должна быть меньше суммы длин других сторон (" +
          str(SIDE_A + SIDE_B) + ") - такого треугольника не существует")
else:
    if SIDE_A == SIDE_B and SIDE_A == SIDE_C:
        print("Треугольник равносторонний")
    elif SIDE_A == SIDE_B or SIDE_A == SIDE_C or SIDE_B == SIDE_C:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник Разносторонний")
