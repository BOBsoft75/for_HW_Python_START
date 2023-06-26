# Была выполнена 1 задача из домашнего задания номер 2.

# Урок 2. Простые типы данных
# 1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = num_first = int(input('Введи целое число: '))
hex_num = ""

while num > 0:
    dec_modul = num % 16
    if dec_modul == 15:
        hex_modul = "f"
    elif dec_modul == 14:
        hex_modul = "e"
    elif dec_modul == 13:
        hex_modul = "d"
    elif dec_modul == 12:
        hex_modul = "c"
    elif dec_modul == 11:
        hex_modul = "b"
    elif dec_modul == 10:
        hex_modul = "a"
    else:
        hex_modul = str(dec_modul)
    hex_num = hex_modul + hex_num
    num //= 16
    print(num, dec_modul)

hex_num = "0x" + hex_num
print("Расчетное шестнадцатеричное представление числа: " + hex_num)
print("Эталонное шестнадцатеричное представление числа: " + hex(num_first))
if hex_num == hex(num_first):
    print("Программа работает корректно.")