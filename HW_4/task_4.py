# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начисление процентов в размере: ",
              percent_add * bank)


def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списание процентов за Cash: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Списание процентов за Cash: ", 600)
    else:
        bank -= cash * percent_take
        print("Списание процентов за Cash: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начисление процентов в размере: ",
              percent_add * bank)


def check_bank() -> int:
    while True:
        cash = int(
            input("Введите сумму опреации кратную 50\n"))
        if cash % 50 == 0:
            return cash
        

def exit_bank():
    print("До новых встреч!\n")
    exit()





list_operation = []

while True:
    action = input(
        "1 - Снять деньги\n2 - Пополнить\n3 - Баланс\n4 - История операций\n5 - Выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списание налога на богатство: ",
                  bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ",
                  bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ",
                  bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
