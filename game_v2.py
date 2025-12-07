"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_find(number: int = 50) -> int:
    """Находим загаданное число бинарным поиском

    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50  # предполагаемое число
    max_number = 100
    min_number = 1

    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min_number = predict_number + 1 #сокращаем минимальную границу, если число больше
            predict_number = (max_number + min_number) // 2 #считаем серединное число нового диапозона
        elif number < predict_number:
            max_number = predict_number - 1 #сокращаем максимальную границу, если число больше
            predict_number = (min_number + max_number) // 2 #считаем серединное число нового диапозона

    return count


def score_game(binary_find) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_find ([type]): функция поиска загаданного числа

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_find(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_find)
