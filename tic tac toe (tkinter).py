import tkinter as tk
from tkinter import messagebox

def sum(a, b, c):
    return a + b + c

def checkWin(xState, zState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            messagebox.showinfo("Game Over", "X Won the match")
            return True
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            messagebox.showinfo("Game Over", "O Won the match")
            return True
    return False

def button_click(index):
    global turn
    if xState[index] == 0 and zState[index] == 0:
        if turn == 1:
            buttons[index].config(text="X")
            xState[index] = 1
        else:
            buttons[index].config(text="O")
            zState[index] = 1

        if checkWin(xState, zState):
            messagebox.showinfo("Game Over", "Match over")
            root.destroy()

        turn = 1 - turn


root = tk.Tk()
root.title("Tic Tac Toe")


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1  
buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
