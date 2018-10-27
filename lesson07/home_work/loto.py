#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class Generator:
    def __init__(self, min, max):
        self.__min = min
        self.__max = max
        self.__remain = [i for i in range(max + 1)]
        self.__remain_count = max

    def __call__(self):
        if self.__remain_count < self.__min:
            return None
        r = random.randint(self.__min, self.__remain_count)
        ret = self.__remain[r]
        self.__remain[r], self.__remain[self.__remain_count] = \
            self.__remain[self.__remain_count], self.__remain[r]
        self.__remain_count -= 1
        return ret


class Ticket: # None: empty, 0: crossed
    def __init__(self, gen):
        self.__cells = [None] * 27
        for line_begin in range(0, 27, 9):
            gen_indexes = Generator(line_begin, line_begin + 8)
            numbers = [gen() for _ in range(5)]
            indexes = [gen_indexes() for _ in range(5)]
            numbers.sort()
            indexes.sort()
            for i in range(5):
                self.__cells[indexes[i]] = numbers[i]

    def str(self):
        ret = '-' * 26 + '\n'
        for i, cell in enumerate(self.__cells):
            s = ''
            if cell is not None:
                s = '-' if cell == 0 else str(cell)
            frmt = '%2s' if i % 9 == 0 else '%3s'
            ret += frmt % s
            if (i + 1) % 9 == 0:
                ret += '\n'
        ret += '-' * 26 + '\n'
        return ret

gen = Generator(1, 90)
ticket = Ticket(gen)
print(ticket.str())

# gen = Generator(1,5)
# print([gen()]*5)
