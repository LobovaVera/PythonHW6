# 77-85 lambda

import sys
import tkinter as tk
from tkinter import *
import time

count = 2
score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
text = ''

win_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8
], [2,4,6]]

def check_the_winner(score_list):
    
    for i in range(0, len(win_list)):
        if score_list[win_list[i][0]] == score_list[win_list[i][1]] == score_list[win_list[i][2]] == 1:
            label1.config(text = "Выиграл О")
            win.update_idletasks()
            time.sleep(5)
            sys. exit()
        elif score_list[win_list[i][0]] == score_list[win_list[i][1]] == score_list[win_list[i][2]] == 2:
            label1.config(text = "Выиграл X")
            win.update_idletasks()
            time.sleep(5)
            sys. exit()
    if any(x == 0 for x in score_list):
        label1.config(text = "Игра продолжается")
        win.update_idletasks()
        
                   
    elif all(x > 0 for x in score_list):
        label1.config(text = "Ничья!")
        win.update_idletasks()
        time.sleep(5)
        sys.exit()
            
win = tk.Tk()
win.title("Крестики-нолики")
photo = tk.PhotoImage(file = 'xo.png')
win.iconphoto(0, photo)
win.resizable(0, 0)

def score(n):
    global text
    global count
    score_list[n] = count
    if count == 1:
        text= 'O'
        count = 2
    else:
        text = 'X'
        count = 1
    
    match n:
        case 0:
            btn1['text'] = f'{text}'
        case 1:
            btn2['text'] = f'{text}'
        case 2:
            btn3['text'] = f'{text}'
        case 3:
            btn4['text'] = f'{text}'
        case 4:
            btn5['text'] = f'{text}'
        case 5:
            btn6['text'] = f'{text}'
        case 6:
            btn7['text'] = f'{text}'
        case 7:
            btn8['text'] = f'{text}'
        case 8:
            btn9['text'] = f'{text}'
        

btn1 = tk.Button(win, text=f'{text}', command=lambda: [score(0), check_the_winner(score_list)] )
btn2 = tk.Button(win, text=f'{text}', command=lambda: [score(1), check_the_winner(score_list)] )
btn3 = tk.Button(win, text=f'{text}', command=lambda: [score(2), check_the_winner(score_list)] )
btn4 = tk.Button(win, text=f'{text}', command=lambda: [score(3), check_the_winner(score_list)] )
btn5 = tk.Button(win, text=f'{text}', command=lambda: [score(4), check_the_winner(score_list)] )
btn6 = tk.Button(win, text=f'{text}', command=lambda: [score(5), check_the_winner(score_list)] )
btn7 = tk.Button(win, text=f'{text}', command=lambda: [score(6), check_the_winner(score_list)] )
btn8 = tk.Button(win, text=f'{text}', command=lambda: [score(7), check_the_winner(score_list)] )
btn9 = tk.Button(win, text=f'{text}', command=lambda: [score(8), check_the_winner(score_list)] )

btn1.grid(row=0, column=0, stick='wens')
btn2.grid(row=0, column=1, stick='wens')
btn3.grid(row=0, column=2, stick='wens')
btn4.grid(row=1, column=0, stick='wens')
btn5.grid(row=1, column=1, stick='wens')
btn6.grid(row=1, column=2, stick='wens')
btn7.grid(row=2, column=0, stick='wens')
btn8.grid(row=2, column=1, stick='wens')
btn9.grid(row=2, column=2, stick='wens')

label1 = tk.Label( win, font=('Calibri 30'))
label1.grid(row = 3, column = 0, columnspan = 3, stick = 'we')


win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)
win.grid_columnconfigure(2, minsize=200)
win.grid_rowconfigure(0, minsize=200)
win.grid_rowconfigure(1, minsize=200)
win.grid_rowconfigure(2, minsize=200)
win.mainloop()


