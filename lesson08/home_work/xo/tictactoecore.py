class TicTacToeCore:
    def __init__(self, size):
        self.__size = size
        self.reset()


    @property
    def current(self):
        return self.__current


    @property
    def game_over(self):
        return self.__game_over


    @property
    def size(self):
        return self.__size

    @property
    def matrix(self):
        return self.__cells


    def reset(self):
        self.__current = 'x'
        self.__game_over = False
        self.__cells = [[None] * self.__size for _ in range(self.__size)]


    def action(self, i, j):
        if self.__game_over:
            return None
        if i < 0 or j < 0 or i >= len(self.__cells) or j >= len(self.__cells):
            return None
        if self.__cells[i][j] != None:
            return None
        self.__cells[i][j] = self.__current
        if self.win():
            return True
        #Add draw
        self.__current = 'o' if self.__current == 'x' else 'x'
        return False


    def win(self):
        ret1 = []
        for i in range(self.__size):
            if len(ret1) >= 5:
                break
            else:
                ret1 = []
            for j in range(self.__size):
                if self.__cells[i][j] == self.__current:
                    ret1.append((i,j))
                else:
                    if len(ret1) >= 5:
                        i = self.__size
                        break
                    ret1 = []
        if len(ret1) < 5:
            ret1 = []

        ret2 = []
        for i in range(self.__size):
            if len(ret2) >= 5:
                break
            else:
                ret2 = []
            for j in range(self.__size):
                if self.__cells[j][i] == self.__current:
                    ret2.append((j,i))
                else:
                    if len(ret2) >= 5:
                        i = self.__size
                        break
                    ret2 = []
        if len(ret2) < 5:
            ret2 = []

        ret3 = []
        for i in range(self.__size):
            for j in range(self.__size):
                if len(ret3) >= 5:
                    break
                else:
                    ret3 = []
                for k in range(self.__size):
                    if i+k >= self.__size or j+k >= self.__size:
                        if len(ret3) >= 5:
                            i = self.__size
                            break
                        ret3 = []
                        break
                    if self.__cells[i+k][j+k] == self.__current:
                        ret3.append((i+k, j+k))
                    else:
                        if len(ret3) >= 5:
                            i = self.__size
                            break
                        ret3 = []
        if len(ret3) < 5:
            ret3 = []

        ret4 = []
        for i in range(self.__size):
            for j in range(self.__size):
                if len(ret4) >= 5:
                    break
                else:
                    ret4 = []
                for k in range(self.__size):
                    if i+k >= self.__size or j-k < 0:
                        if len(ret4) >= 5:
                            i = self.__size
                            break
                        ret4 = []
                        break
                    if self.__cells[i+k][j-k] == self.__current:
                        ret4.append((i+k, j-k))
                    else:
                        if len(ret4) >= 5:
                            i = self.__size
                            break
                        ret4 = []
        if len(ret4) < 5:
            ret4 = []

        ret = ret1 + ret2 + ret3 + ret4
        if len(ret) == 0:
            return None

        self.__game_over = True
       # self.win()
        return ret
