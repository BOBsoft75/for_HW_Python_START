# Была выполнена задача из семинара номер 1.

# Таблица умножения

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{j:3} *{i:3} = {i * j:1} \t', end='')
    print('')
else:
    print("Таблица умножения до 10")