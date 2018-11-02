import tkinter as tk
from tictactoecore import TicTacToeCore

import winsound

def beep(freq, dur):
    #winsound.Beep(freq, dur)
    pass

G_SIZE = 10
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
    def rand_action(self, matrix):
        while True:
            i = random.randint(0, G_SIZE - 1)
            j = random.randint(0, G_SIZE - 1)
            if matrix[i][j] is None:
                return (i, j)

    def action(self, matrix, cur):
        not_cur = 'x' if cur == 'o' else 'o'

        for i in range(G_SIZE):
            for j in range(G_SIZE):
                if self.__win(matrix, i, j, cur):
                    return (i, j)

        for i in range(G_SIZE):
            for j in range(G_SIZE):
                if self.__win(matrix, i, j, not_cur):
                    return (i, j)

        for i in range(G_SIZE):
            for j in range(G_SIZE):
                if self.__win2(matrix, i, j, cur):
                    return (i, j)

        for i in range(G_SIZE):
            for j in range(G_SIZE):
                if self.__win2(matrix, i, j, not_cur):
                    return (i, j)

        return self.rand_action(matrix)


    def __win2(self, matrix, i, j, cur):
        if matrix[i][j] is not None:
            return None

        for i in range(G_SIZE):
            for j in range(G_SIZE):
                if matrix[i][j] is not None: continue
                matrix[i][j] = cur
                if self.__win(matrix, i, j, cur):
                    for ii in range(G_SIZE):
                        counter = 0
                        for jj in range(G_SIZE):
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


    def run(self):
        self.__root.mainloop()


    def __change_player(self, event):
        but = event.widget
        but['text'] = 'Player' if but['text'] == 'AI' else 'AI'
        beep(150, 75)

    def __action(self, i, j):
        but = self.__buttons[i][j]
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

    def __clicked(self, event):
        if self.__ttt.game_over:
            self.__ttt.win()


        but = event.widget
        if but['state'] == 'disabled':
            return
        grid_info = but.grid_info()
        i, j = grid_info['row'], grid_info['column']
        self.__action(i, j)

        if self.__ttt.current == 'o' and self.__button2['text'] == 'AI':
            ai = Ai()
            i, j = ai.action(self.__ttt.matrix, self.__ttt.current)
            self.__action(i, j)


    def __set_buttons_state(self, val):
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__buttons[i][j]['state'] = 'normal' if val else 'disabled'
        #state = 'normal' if val else 'disabled'
        #self.__for_each(self, lambda self, but, state: but['state']=state)


    def __reset(self):
        self.__set_buttons_state(True)
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__ttt.reset()
                but = self.__buttons[i][j]
                but['text'] = ''
                but['background'] = self.__root.cget("background")
        beep(700, 75)
    # def __for_each(self, fun, *args):
    #     for i in range(self.__ttt.size):
    #         for j in range(self.__ttt.size):
    #             fun(self.__buttons[i][j], args)



if __name__ == "__main__":
    ttt = TicTacToe(G_SIZE)
    ttt.run()
