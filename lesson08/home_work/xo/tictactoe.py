import tkinter as tk
import threading
from tictactoecore import TicTacToeCore

import winsound

def beep(freq, dur):
    threading.Thread(target=lambda: winsound.Beep(freq, dur)).start()

G_SIZE = 20
G_BUTTON_SIZE = 1

import random
class StupidAi:
    def action(self, matrix):
        while True:
            i = random.randint(0, G_SIZE - 1)
            j = random.randint(0, G_SIZE - 1)
            if matrix[i][j] is None:
                return (i, j)
        return None


class Ai:
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

        for ii in range(-2, 3):
            for jj in range(-2, 3):
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


        ret = self.rand_action(matrix)
        return ret


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




class TicTacToe:
    def __init__(self, size):
        self.__root = tk.Tk()
        self.__frame = tk.Frame(self.__root)
        self.__frame.pack()
        self.__root.resizable(0,0)
        self.__root.wm_title('Tic-Tac-Toe')
        img_arg = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='
        self.__empty_img = tk.PhotoImage(img_arg)
        self.__ttt = TicTacToeCore(size)
        self.__cong = False

        self.__buttons = [[None] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                #self.__buttons[i][j] = tk.Button(self.__frame, image=self.__empty_img, height=24, width=24, disabledforeground="blue", font=('', 10, 'bold'), compound="center")
                self.__buttons[i][j] = tk.Button(self.__frame, height=1, width=2, disabledforeground="blue", font=('', 10, 'bold'))
                self.__buttons[i][j].grid(row=i, column=j)
                self.__buttons[i][j].bind('<Button>', self.__clicked)

        self.__button1 = tk.Button(self.__frame, text="Player", fg="blue", activeforeground='blue')
        self.__button1.grid(row=size, column=0, columnspan=2)
        self.__button1.bind('<Button>', self.__change_player)

        self.__button2 = tk.Button(self.__frame, text="Player", fg="red", activeforeground='red')
        self.__button2.grid(row=size, column=size-2, columnspan=2)
        self.__button2.bind('<Button>', self.__change_player)

        self.__new_res = tk.Button(self.__frame, text="New", command=self.__reset)
        self.__new_res.grid(row=size, column=(size-1)//2, columnspan=2)

        self.__ai = Ai()
        self.__mutex = threading.Lock()


    def run(self):
        self.__root.mainloop()


    def __change_player(self, event):
        but = event.widget
        but['text'] = 'Player' if but['text'] == 'AI' else 'AI'
        beep(150, 75)
        self.__ai_if_need()

    def __action(self, i, j):
        but = self.__buttons[i][j]
        self.__ai.lst_append(self.__ttt.matrix, i, j)
        grid_info = but.grid_info()
        current = self.__ttt.current
        go = self.__ttt.game_over
        if self.__ttt.action(i,j) != None:
            x_turn = current == 'x'
            but['text'] = '✕' if x_turn else '◯'
            but['disabledforeground'] = 'blue' if x_turn else 'red'
            but['state'] = 'disabled'
            freq = 350 if x_turn else 300
            if not self.__ttt.win():
                beep(freq, 200)
        win_cells = self.__ttt.win()
        if win_cells is not None and not go:
            self.__set_buttons_state(False)
            bg = 'orange' if self.__ttt.current == 'x' else 'yellow green'
            for cell in win_cells:
                self.__buttons[cell[0]][cell[1]]['background'] = bg
            beep(400, 500)

    def __ai_if_need(self):
        if self.__ttt.current == 'x' and self.__button1['text'] == 'AI' or \
                self.__ttt.current == 'o' and self.__button2['text'] == 'AI':
            def action():
                with self.__mutex:
                    i, j = self.__ai.action(self.__ttt.matrix, self.__ttt.current)
                    self.__action(i, j)
                    self.__ai_if_need()

            threading.Thread(target=action).start()

    def __clicked(self, event):
            if self.__ttt.game_over:
                self.__ttt.win()

            if self.__mutex.locked():
                return

            but = event.widget
            if but['state'] == 'disabled':
                return

            grid_info = but.grid_info()
            i, j = grid_info['row'], grid_info['column']
            self.__action(i, j)

            self.__ai_if_need()

    def __set_buttons_state(self, val):
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__buttons[i][j]['state'] = 'normal' if val else 'disabled'
        #state = 'normal' if val else 'disabled'
        #self.__for_each(self, lambda self, but, state: but['state']=state)


    def __reset(self):
        self.__set_buttons_state(True)
        self.__ai.reset()
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__ttt.reset()
                but = self.__buttons[i][j]
                but['text'] = ''
                but['background'] = self.__root.cget("background")
        beep(700, 75)
        self.__ai_if_need()
    # def __for_each(self, fun, *args):
    #     for i in range(self.__ttt.size):
    #         for j in range(self.__ttt.size):
    #             fun(self.__buttons[i][j], args)



if __name__ == "__main__":
    ttt = TicTacToe(G_SIZE)
    ttt.run()
