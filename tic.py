#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:03:56 2023

@author: sibaamani
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        #وظیفه این متد ایجاد یک بازی جدید با استفاده از تیک نتر است

        # Create a frame to hold the game widgets
        self.game_frame = tk.Frame(root, bg="blue", padx=10, pady=10, bd=5)
        self.game_frame.pack()

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.game_frame, text="", width=10, height=2,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def make_move(self, row, col):
        #این متد برای انجام حرکات بازی است در صورتی که حرکت معتبر باشد انجام می شو و برنده بازی برسی می شود
        if self.board[row * 3 + col] == "" and not self.check_winner():
            self.board[row * 3 + col] = self.current_player
            if self.current_player == "X":
                self.buttons[row * 3 + col].config(text="X", fg="green")
            else:
                self.buttons[row * 3 + col].config(text="O", fg="red")

            if self.check_winner():
                #این متد برای بررسی برنده بازی است در صورت وجود برند مقدار برگشت می شود
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        #این متد برای بررسی برنده بازی است در صورت وجود برند مقدار برگشت می شود
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and self.board[combo[0]] != "":
                return True
        return False

    def reset_game(self):
        #این متد برای مجدد بازی است و صفحه را به حالت اولیه بر می گر
        
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="", fg="black")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
