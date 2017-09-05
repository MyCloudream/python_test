#! /usr/bin/env python
# coding: UTF-8
# python3.3

from tkinter import *
import tkinter as tk
from tkinter.messagebox import askquestion
from tkinter.messagebox import showinfo
import time
import random

import model

# just used by backward function
matrix_stack = [] 
# just used by forward function
matrix_stack_forward = []

class Application():
    def __init__(self, root):
        '''
        Init Form
        '''
        self.root = root
        self.createFrameTop()
        self.createFrameMiddle()
        self.createFrameBottom()
        self.matrix = model.init()
        matrix_stack.append(self.matrix)
        matrix_stack_forward.append(self.matrix)
        self.btn_show_matrix(self.matrix)
        self.root.bind("<KeyPress> ", self.bind_key)

    def createFrameTop(self):
        '''
        Create LabelFrame Top
        '''
        show_list = ["Score:", "0", "Step:", "0"]

        self.frm_top = tk.LabelFrame(self.root, font=('Tempus Sans ITC', 10))
        self.frm_top.grid(row = 0, column = 0, padx = 15, pady = 2,sticky = "wesn")

        self.label_top_list = []
        for (i, operate) in enumerate(show_list):
            label_top = tk.Label(self.frm_top, width = 15, height=2, text=show_list[i], font=('Tempus Sans ITC', 10))
            label_top.grid(row = i//4, column = i%4, padx = 5, pady = 2, sticky = "wesn")
            self.label_top_list.append(label_top)

    def createFrameMiddle(self):
        '''
        Create LabelFrame Middle
        '''
        self.frm_middle = tk.LabelFrame(self.root, font=('Tempus Sans ITC', 10))
        self.frm_middle.grid(row = 1, column = 0, padx = 15, pady = 2, sticky = "wesn")

        self.createFrameMiddleLeft()
        self.createFrameMiddleRight()

    def createFrameMiddleLeft(self):
        '''
        Create LabelFrame Middle Left
        '''
        self.frm_middle_left = tk.LabelFrame(self.frm_middle, font=('Tempus Sans ITC', 10))
        self.frm_middle_left.grid(row = 0, column = 0, padx = 5, pady = 2,sticky = "wesn")

        self.btn_middle_list = []
        for i in range(16):
            entry_bottom = tk.Button(self.frm_middle_left, width = 5, height=2, font=('Tempus Sans ITC', 10))
            entry_bottom.grid(row = i//4, column = i%4, padx = 5, pady = 3, sticky = "wesn")
            self.btn_middle_list.append(entry_bottom)

    def createFrameMiddleRight(self):
        '''
        Create LabelFrame Middle Right
        '''
        operate_list = ["Operating Instructions:", 
                        "↑    --    Up", "↓    --    Down", "←    --    Left", "→    --    Right",
                        "b    --    Backward", "f    --    Forward", "q    --    Quit"]

        self.frm_middle_right = tk.LabelFrame(self.frm_middle, font=('Tempus Sans ITC', 10))
        self.frm_middle_right.grid(row = 0, column = 1, padx = 5, pady = 2,sticky = "wesn")

        for (i, operate) in enumerate(operate_list):
            label_middle_right = tk.Label(self.frm_middle_right, width=30, height=1, text=operate, font=('Tempus Sans ITC', 10))
            label_middle_right.grid(row = i, column = 0, padx = 5, pady = 2, sticky = "w")

    def createFrameBottom(self):
        '''
        Create LabelFrame Bottom
        '''
        show_list = ["Time:", "0", "0"]

        self.frm_bottom = tk.LabelFrame(self.root, font=('Tempus Sans ITC', 10))
        self.frm_bottom.grid(row = 2, column = 0, padx = 15, pady = 2, sticky = "wesn")

        self.label_bottom_list = []
        for (i, operate) in enumerate(show_list):
            label_bottom = tk.Label(self.frm_bottom, width = (i+1)*12, height=2, text=show_list[i], font=('Tempus Sans ITC', 8))
            label_bottom.grid(row = i//3, column = i%3, padx = 5, pady = 2, sticky = "w")
            self.label_bottom_list.append(label_bottom)
        self.show_time()

    def bind_key(self, event):
        '''
        key event
        '''
        if model.is_over(self.matrix):
            if askquestion("GAME OVER","GAME OVER!\nDo you want to init it?") == 'yes':
                self.matrix = my_init()
                self.btn_show_matrix(self.matrix)
                return
            else:
                self.root.destroy()
        else:
            if event.keysym.lower() == "q":
                self.root.destroy()
            elif event.keysym == "Left":
                self.matrix = model.move_left(self.matrix)
            elif event.keysym == "Right":
                self.matrix = model.move_right(self.matrix)
            elif event.keysym == "Up":
                self.matrix = model.move_up(self.matrix)
            elif event.keysym == "Down":
                self.matrix = model.move_down(self.matrix)
            elif event.keysym.lower() == "b":
                if len(matrix_stack) == 1:
                    showinfo('info', 'Cannot back anymore...')
                else:
                    matrix_stack_forward.append(self.matrix)
                    matrix_stack.pop()
                    self.matrix = matrix_stack[-1]
            elif event.keysym.lower() == "f":
                if len(matrix_stack_forward) == 0:
                    showinfo('info', 'Cannot forward anymore...')
                else:
                    self.matrix = matrix_stack_forward[-1]
                    matrix_stack_forward.pop()
                    matrix_stack.append(self.matrix)
                       
            if event.keysym in ["q", "Left", "Right", "Up", "Down"]:
                try:
                    self.matrix = model.insert(self.matrix)
                    matrix_stack.append(self.matrix)
                    del matrix_stack_forward[0:]
                except:
                    pass
            try:
                self.btn_show_matrix(self.matrix)
            except:
                pass

        if model.is_win(self.matrix):
            if askquestion("WIN","You win the game!\nDo you want to init it?") == 'yes':
                self.matrix = my_init()
                self.btn_show_matrix(self.matrix)
                return
            else:
                self.root.destroy()

    def btn_show_matrix(self, matrix):
        '''
        show matrix
        '''
        for (i,btn_item) in enumerate(self.btn_middle_list):
            btn_item['text'] = matrix[i//4][i%4]

        for (i,btn_item) in enumerate(self.btn_middle_list):
            if int(btn_item['text']) < 64:
                btn_item['fg'] = 'red'
            elif int(btn_item['text']) < 512:
                btn_item['fg'] = 'blue'
            else:
                btn_item['fg'] = 'green'
            if int(btn_item['text']) == 0:
                btn_item['text'] = ''

        step = len(matrix_stack) - 1
        self.label_top_list[3]['text'] = step

    def show_time(self):
        '''
        Displays the current time
        '''
        now = str(time.strftime('%Y-%m-%d %H:%M:%S'))
        self.label_bottom_list[2].config(text=now)
        self.root.after(1024, self.show_time)

if __name__=="__main__":
    '''
    main loop
    '''
    root = tk.Tk()
    root.title("2048")
    root.iconbitmap('2048.ico')
    Application(root)
    # Set maximize invalid
    root.resizable(False,False)
    root.mainloop()