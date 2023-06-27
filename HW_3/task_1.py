# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 3, 5, 2, 17, 1, 17, 4, 2, 9, 5, 6]
res_list = []

for item in my_list:
    if my_list.count(item) > 1 and item not in res_list:
        res_list.append(item)

print(f'Исходный список: ', str(my_list))
print(f'Итоговый список: ', str(res_list))