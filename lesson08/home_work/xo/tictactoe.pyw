import tkinter as tk
import time
import os
import threading
from tictactoecore import TicTacToeCore
from tictactoeai import TicTacToeAi

if os.name == 'nt':
    import winsound
    def beep(freq, dur):
        threading.Thread(target=lambda: winsound.Beep(freq, dur)).start()
    G_BUTTON_WIDTH = 2
    G_BUTTON_HEIGHT = 1
else:
    def beep(freq, dur):
        pass
    G_BUTTON_WIDTH = 1
    G_BUTTON_HEIGHT = 1

G_SIZE = 15


class TicTacToe:
    def __init__(self, size):
        self.__root = tk.Tk()
        self.__frame = tk.Frame(self.__root)
        self.__frame.pack()
        self.__root.resizable(0,0)
        self.__root.wm_title('Tic-Tac-Toe')
        self.__ttt = TicTacToeCore(size)
        self.__cong = False

        self.__buttons = [[None] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                self.__buttons[i][j] = tk.Button(self.__frame, width=G_BUTTON_WIDTH, height=G_BUTTON_HEIGHT, disabledforeground="blue", font=('', 10, 'bold'))
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

        self.__ai = TicTacToeAi()
        self.__mutex = threading.Lock()


    def run(self):
        threading.Thread(target=self.__run_ai).start()
        self.__root.mainloop()


    def __change_player(self, event):
        but = event.widget
        but['text'] = 'Player' if but['text'] == 'AI' else 'AI'
        beep(150, 75)


    def __action(self, i, j):
        if self.__ttt.game_over:
            return

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


    def __run_ai(self):
        while True:
            if (self.__ttt.current == 'x' and self.__button1['text'] == 'AI' or \
                self.__ttt.current == 'o' and self.__button2['text'] == 'AI') and \
                not self.__ttt.game_over:
                with self.__mutex:
                    i, j = self.__ai.action(self.__ttt.matrix, self.__ttt.current)
                    self.__action(i, j)
                time.sleep(0.1)


    def __clicked(self, event):
        if self.__mutex.locked():
            return

        if self.__ttt.current == 'x' and self.__button1['text'] == 'AI' or \
           self.__ttt.current == 'o' and self.__button2['text'] == 'AI':
           return

        but = event.widget
        if but['state'] == 'disabled':
            return

        grid_info = but.grid_info()
        i, j = grid_info['row'], grid_info['column']
        self.__action(i, j)

    def __set_buttons_state(self, val):
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__buttons[i][j]['state'] = 'normal' if val else 'disabled'

    def __reset(self):
        if self.__mutex.locked(): return
        self.__set_buttons_state(True)
        self.__ttt.reset()
        self.__ai.reset()
        for i in range(self.__ttt.size):
            for j in range(self.__ttt.size):
                self.__ttt.reset()
                but = self.__buttons[i][j]
                but['text'] = ''
                but['background'] = self.__root.cget("background")
        beep(700, 75)



if __name__ == "__main__":
    ttt = TicTacToe(G_SIZE)
    ttt.run()
