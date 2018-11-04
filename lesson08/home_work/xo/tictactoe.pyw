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
        self._root = tk.Tk()
        self._frame = tk.Frame(self._root)
        self._frame.pack()
        self._root.resizable(0,0)
        self._root.wm_title('Tic-Tac-Toe')
        self._ttt = TicTacToeCore(size)
        self._cong = False

        self._buttons = [[None] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                self._buttons[i][j] = tk.Button(self._frame, width=G_BUTTON_WIDTH, height=G_BUTTON_HEIGHT, disabledforeground="blue", font=('', 10, 'bold'))
                self._buttons[i][j].grid(row=i, column=j)
                self._buttons[i][j].bind('<Button>', self._clicked)

        self._button1 = tk.Button(self._frame, text="Player", fg="blue", activeforeground='blue')
        self._button1.grid(row=size, column=0, columnspan=2)
        self._button1.bind('<Button>', self._change_player)

        self._button2 = tk.Button(self._frame, text="Player", fg="red", activeforeground='red')
        self._button2.grid(row=size, column=size-2, columnspan=2)
        self._button2.bind('<Button>', self._change_player)

        self._new_res = tk.Button(self._frame, text="New", command=self._reset)
        self._new_res.grid(row=size, column=(size-1)//2, columnspan=2)

        self._ai = TicTacToeAi()
        self._mutex = threading.Lock()


    def run(self):
        threading.Thread(target=self._run_ai).start()
        self._root.mainloop()


    def _change_player(self, event):
        but = event.widget
        but['text'] = 'Player' if but['text'] == 'AI' else 'AI'
        beep(150, 75)


    def _action(self, i, j):
        if self._ttt.game_over:
            return

        but = self._buttons[i][j]
        self._ai.lst_append(self._ttt.matrix, i, j)
        grid_info = but.grid_info()
        current = self._ttt.current
        go = self._ttt.game_over
        if self._ttt.action(i,j) != None:
            x_turn = current == 'x'
            but['text'] = '✕' if x_turn else '◯'
            but['disabledforeground'] = 'blue' if x_turn else 'red'
            but['state'] = 'disabled'
            freq = 350 if x_turn else 300
            if not self._ttt.win():
                beep(freq, 200)
        win_cells = self._ttt.win()
        if win_cells is not None and not go:
            self._set_buttons_state(False)
            bg = 'orange' if self._ttt.current == 'x' else 'yellow green'
            for cell in win_cells:
                self._buttons[cell[0]][cell[1]]['background'] = bg
            beep(400, 500)


    def _run_ai(self):
        while True:
            if (self._ttt.current == 'x' and self._button1['text'] == 'AI' or \
                self._ttt.current == 'o' and self._button2['text'] == 'AI') and \
                not self._ttt.game_over:
                with self._mutex:
                    i, j = self._ai.action(self._ttt.matrix, self._ttt.current)
                    self._action(i, j)
                time.sleep(0.1)


    def _clicked(self, event):
        if self._mutex.locked():
            return

        if self._ttt.current == 'x' and self._button1['text'] == 'AI' or \
           self._ttt.current == 'o' and self._button2['text'] == 'AI':
           return

        but = event.widget
        if but['state'] == 'disabled':
            return

        grid_info = but.grid_info()
        i, j = grid_info['row'], grid_info['column']
        self._action(i, j)

    def _set_buttons_state(self, val):
        for i in range(self._ttt.size):
            for j in range(self._ttt.size):
                self._buttons[i][j]['state'] = 'normal' if val else 'disabled'

    def _reset(self):
        if self._mutex.locked(): return
        self._set_buttons_state(True)
        self._ttt.reset()
        self._ai.reset()
        for i in range(self._ttt.size):
            for j in range(self._ttt.size):
                self._ttt.reset()
                but = self._buttons[i][j]
                but['text'] = ''
                but['background'] = self._root.cget("background")
        beep(700, 75)



if __name__ == "__main__":
    ttt = TicTacToe(G_SIZE)
    ttt.run()
