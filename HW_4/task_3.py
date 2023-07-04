# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление. .


def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(name='Иван', surname='Петров', weight=80.5,
                     months=['January', 'February', 'March'],
                     cars={'BMW': 'Skoda', 'KIA': 'HAVAL'}))