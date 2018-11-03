import random

class TicTacToeAi:
    def __init__(self):
        self.__lst = []

    def reset(self):
        self.__lst.clear()

    def rand_action(self, matrix):
        size = len(matrix)

        if len(self.__lst) == 0:
            return (size // 2, size // 2)

        while True:
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)

            if ((i, j)) not in self.__lst:
                continue

            if matrix[i][j] is None:
                return (i, j)



    def lst_append(self, matrix, i, j):
        size = len(matrix)

        if (i, j) in self.__lst:
            self.__lst.remove((i,j))

        around = 1
        for ii in range(-around, around+1):
            for jj in range(-around, around+1):
                if i+ii < 0 or j+jj < 0 or i+ii >= size or j+jj >= size or (ii == 0 and jj == 0):
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

        size = len(matrix)

        matrix[i][j] = cur
        counter = 0
        for ii in range(i-5, i+6):
            for jj in range(j-5, j+6):
                if ii<0 or jj<0 or ii>=size or jj>=size or (ii==i and jj==j):
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

        size = len(matrix)

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
            if ii<0 or jj<0 or ii>=size or jj>=size:
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
            if ii<0 or jj<0 or ii>=size or jj>=size:
                continue

            match = (ii == i and jj == j) or matrix[ii][jj] == cur
            if match:
                counter += 1
            if counter == 5:
                return True
            if not match:
                counter = 0

        return False
