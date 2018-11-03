import tkinter as tk
import threading
from tictactoecore import TicTacToeCore

import winsound

G_SIZE = 15

import random

class TicTacToeAi:
    def __init__(self):
        self.__lst = []

    def reset(self):
        self.__lst.clear()

    def rand_action(self, matrix):
        if len(self.__lst) == 0:
            return (G_SIZE // 2, G_SIZE // 2) ###
        while True:
            i = random.randint(0, G_SIZE - 1)
            j = random.randint(0, G_SIZE - 1)

            if ((i, j)) not in self.__lst:
                continue

            if matrix[i][j] is None:
                return (i, j)



    def lst_append(self, matrix, i, j):
        if (i, j) in self.__lst:
            self.__lst.remove((i,j))

        around = 1
        for ii in range(-around, around+1):
            for jj in range(-around, around+1):
                if i+ii < 0 or j+jj < 0 or i+ii >= G_SIZE or j+jj >= G_SIZE or (ii == 0 and jj == 0):
                    continue
                if matrix[i+ii][j+jj] is not None:
                    continue
                if (i+ii, j+jj) not in self.__lst:
                    self.__lst.append((i+ii, j+jj))

    def action(self, matrix, cur):
        not_cur = 'x' if cur == 'o' else 'o'

        for ij in self.__lst:
            if self.__win(matrix, ij[0], ij[1], cur):
                return (ij[0], ij[1])

        for ij in self.__lst:
            if self.__win(matrix, ij[0], ij[1], not_cur):
                return (ij[0], ij[1])

        for ij in self.__lst:
            if self.__win2(matrix, ij[0], ij[1], cur):
                return (ij[0], ij[1])

        for ij in self.__lst:
            if self.__win2(matrix, ij[0], ij[1], not_cur):
                return (ij[0], ij[1])


        return self.rand_action(matrix)


    def __win2(self, matrix, i, j, cur):
        if matrix[i][j] is not None:
            return None

        if ((i, j)) not in self.__lst:
            return None

        matrix[i][j] = cur
        counter = 0
        for ii in range(i-5, i+6):
            for jj in range(j-5, j+6):
                if ii < 0 or jj < 0 or ii>=G_SIZE or jj>=G_SIZE or (ii==i and jj==j):
                    continue
                if self.__win(matrix, ii, jj, cur):
                    counter += 1
            if counter == 2:
                matrix[i][j] = None
                return True
        matrix[i][j] = None
        return False


    def __win(self, matrix, i, j, cur):
        if matrix[i][j] is not None:
            return None

        counter = 0
        for ii in range(i - 4, i + 5):
            if ii < 0: continue
            if ii >= len(matrix): break
            match = ii == i or matrix[ii][j] == cur
            if match:
                counter += 1
            if counter == 5:
                return True
            if not match:
                counter = 0

        counter = 0
        for jj in range(j - 4, j + 5):
            if jj < 0: continue
            if jj >= len(matrix): break
            match = jj == j or matrix[i][jj] == cur
            if match:
                counter += 1
            if counter == 5:
                return True
            if not match:
                counter = 0

        counter = 0
        for kk in range(-4, 5):
            ii = i + kk
            jj = j + kk
            if ii<0 or jj<0 or ii>=G_SIZE or jj>=G_SIZE:
                continue

            match = (ii == i and jj == j) or matrix[ii][jj] == cur
            if match:
                counter += 1
            if counter == 5:
                return True
            if not match:
                counter = 0

        counter = 0
        for kk in range(-4, 5):
            ii = i + kk
            jj = j - kk
            if ii<0 or jj<0 or ii>=G_SIZE or jj>=G_SIZE:
                continue

            match = (ii == i and jj == j) or matrix[ii][jj] == cur
            if match:
                counter += 1
            if counter == 5:
                return True
            if not match:
                counter = 0

        return False
