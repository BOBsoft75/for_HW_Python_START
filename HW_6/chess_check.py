"""Модуль проверки расстановок на шахматной доске
Ферзь бьет фигуру, если она находиться на одной с ним вертикали, горизонтали или диагонали
Ситуацию указания двух ферзей на одной клетке не обрабатываем
"""
import random as rnd

__all__ = ['queen_check', 'generate_positions']

_QUEEN_COUNT: int = 8  # максимальное кол-во ферзей
_BOARD_SIZE: int = 8  # размер доски


def queen_check(positions: list[tuple]) -> bool:
    """Проверка задачи о ферзях.
    :positions: позиции ферзей - кортежи (строка, столбец)
    """
    result = True

    if len(positions) != _QUEEN_COUNT:
        result = False
    else:
        # перебор ферзей по списку, исключая последнего
        for i in range(_QUEEN_COUNT - 1):
            if not result:
                break
            row_1, col_1 = positions[i]
            # проверка со следующими до конца списка
            for j in range(i + 1, _QUEEN_COUNT):
                row_2, col_2 = positions[j]
                # Ферзи на одной линии, если координаты строки или столбца у них равны.
                # Ферзи на одной диагонали, если позицию второго можно получить из позиции первого смещением на равное
                # количество строк и столбцов в любую из сторон
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def generate_positions() -> list[tuple[int, int]]:
    """Генератор позиций ферзей. Генерирует _QUEEN_COUNT позиций, по одному ферзю на строку.
    Для доски с размером стороны _BOARD_SIZE
    """
    result = []
    for i in range(_BOARD_SIZE):
        result.append((i, rnd.randint(0, _BOARD_SIZE - 1)))
    return result
