# Создайте несколько переменных, которые заканчиваются и не оканчиваются на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


bars = "Begin"
str_words = "World"
nums = 50
word = "GeekBrains"
kiss = "cat"
s = "Victory"


def replace_s_var():
    global bars, str_words, nums, word, kiss, s
    s_vars = []  # получение списка переменных, оканчивающихся на s
    for var_name in list(globals().keys()):
        if var_name.endswith('s') and var_name != 's':
            s_vars.append(var_name)

    # перенос значения из переменных на новые переменные без s на конце
    for s_var_name in s_vars:
        var_value = globals()[s_var_name]
        new_var_name = s_var_name[:-1]

    globals()[new_var_name] = var_value

    # замена значения переменных, оканчивающихся на s, на None
    for var_name in s_vars:
        globals()[var_name] = None

    print(bars, str_words, nums, word, kiss, s, s_vars, sep='\n')


replace_s_var()
