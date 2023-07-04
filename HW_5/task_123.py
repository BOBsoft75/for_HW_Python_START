# Задача 1
# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


import os

print('Задача 1')
string = "J:/GeekBrains/PythonDeep(Seminars)/HW_5/task_123.py"

def func_path(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходный путь: {string} \nКортеж из пути: {func_path(string)}')


# Задача 2
# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


print('\nЗадача 2')
names = ['Иван', 'Петр', "Семен"]
salaries = [50000, 40000, 45000]
awards = ['10.25%', '7.25%', '8.50%']
print(f'Исходные данные:\n{names}\n{salaries}\n{awards}')
print('Результат:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})


# Задача 3
# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


print('\nЗадача 3')
a = int(input('Введите число для генератора Фибоначчи: '))


def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibo(a)))