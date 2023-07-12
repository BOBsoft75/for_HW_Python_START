"""Главный модуль программы"""

import chess_check as chess

# Необходимое кол-во успешных расстановок
_GOOD_POSITIONS = 4

if __name__ == "__main__":
    queens_positions = [
        [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]

    # проверка наличия ферзей под ударом
    for list_position in queens_positions:
        print(list_position)
        if chess.queen_check(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")

    # генерация позиций ферзей
    total_case_generated = 0  # всего расстановок сгенерировано
    good_case = 0  # удачных расстановок ферзей из всех сгенерированных
    list_good_positions = []  # список удачных расстановок ферзей

    while good_case < _GOOD_POSITIONS:
        generated_position = chess.generate_positions()
        total_case_generated += 1
        if chess.queen_check(generated_position):
            good_case += 1
            list_good_positions.append(generated_position)

    print(
        f" Всего вариантов сгенерировано {total_case_generated}, удачные расстановки:")
    for pos in list_good_positions:
        print(pos)
