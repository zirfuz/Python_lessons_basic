class TicTacToeCore:
    def __init__(self, size):
        self._size = size
        self.reset()

    @property
    def current(self):
        return self._current

    @property
    def game_over(self):
        return self._game_over

    @property
    def size(self):
        return self._size

    @property
    def matrix(self):
        return self._cells


    def reset(self):
        self._current = 'x'
        self._game_over = False
        self._cells = [[None] * self._size for _ in range(self._size)]


    def action(self, i, j):
        if self._game_over:
            return None
        if i < 0 or j < 0 or i >= len(self._cells) or j >= len(self._cells):
            return None
        if self._cells[i][j] != None:
            return None
        self._cells[i][j] = self._current
        if self.win():
            return True

        #Add draw

        self._current = 'o' if self._current == 'x' else 'x'
        return False


    def win(self):
        ret1 = []
        for i in range(self._size):
            if len(ret1) >= 5:
                break
            else:
                ret1 = []
            for j in range(self._size):
                if self._cells[i][j] == self._current:
                    ret1.append((i,j))
                else:
                    if len(ret1) >= 5:
                        i = self._size
                        break
                    ret1 = []
        if len(ret1) < 5:
            ret1 = []

        ret2 = []
        for i in range(self._size):
            if len(ret2) >= 5:
                break
            else:
                ret2 = []
            for j in range(self._size):
                if self._cells[j][i] == self._current:
                    ret2.append((j,i))
                else:
                    if len(ret2) >= 5:
                        i = self._size
                        break
                    ret2 = []
        if len(ret2) < 5:
            ret2 = []

        ret3 = []
        for i in range(self._size):
            for j in range(self._size):
                if len(ret3) >= 5:
                    break
                else:
                    ret3 = []
                for k in range(self._size):
                    if i+k >= self._size or j+k >= self._size:
                        if len(ret3) >= 5:
                            i = self._size
                            break
                        ret3 = []
                        break
                    if self._cells[i+k][j+k] == self._current:
                        ret3.append((i+k, j+k))
                    else:
                        if len(ret3) >= 5:
                            i = self._size
                            break
                        ret3 = []
        if len(ret3) < 5:
            ret3 = []

        ret4 = []
        for i in range(self._size):
            for j in range(self._size):
                if len(ret4) >= 5:
                    break
                else:
                    ret4 = []
                for k in range(self._size):
                    if i+k >= self._size or j-k < 0:
                        if len(ret4) >= 5:
                            i = self._size
                            break
                        ret4 = []
                        break
                    if self._cells[i+k][j-k] == self._current:
                        ret4.append((i+k, j-k))
                    else:
                        if len(ret4) >= 5:
                            i = self._size
                            break
                        ret4 = []
        if len(ret4) < 5:
            ret4 = []

        ret = ret1 + ret2 + ret3 + ret4
        if len(ret) == 0:
            return None

        self._game_over = True
        return ret
