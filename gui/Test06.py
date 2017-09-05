#!/usr/bin/python3
# -*-coding:utf-8-*-
import tkinter
import tkinter.font


class Calculate():
    def __init__(self):
        self.tk = tkinter.Tk();
        self.tk.title("Calculate");
        self.tk.resizable(0, 0);
        self.showfont = tkinter.font.Font(self.tk, size=26);
        self.sysfont = tkinter.font.Font(self.tk, size=16);
        self.entry = tkinter.Entry(self.tk, width=20, font=self.showfont, background="#ffffff");
        self.entry.grid(row=0, column=0, columnspan=4, pady=10);
        self.btn1 = tkinter.Button(self.tk, text="1", font=self.sysfont);
        self.btn1.grid(row=1, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);
        self.btn2 = tkinter.Button(self.tk, text="2", font=self.sysfont);
        self.btn2.grid(row=1, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);
        self.btn3 = tkinter.Button(self.tk, text="3", font=self.sysfont);
        self.btn3.grid(row=1, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_divide = tkinter.Button(self.tk, text="÷", font=self.sysfont);
        self.btn_divide.grid(row=1, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn4 = tkinter.Button(self.tk, text="4", font=self.sysfont);
        self.btn4.grid(row=2, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn5 = tkinter.Button(self.tk, text="5", font=self.sysfont);
        self.btn5.grid(row=2, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn6 = tkinter.Button(self.tk, text="6", font=self.sysfont);
        self.btn6.grid(row=2, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_mult = tkinter.Button(self.tk, text="×", font=self.sysfont);
        self.btn_mult.grid(row=2, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn7 = tkinter.Button(self.tk, text="7", font=self.sysfont);
        self.btn7.grid(row=3, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn8 = tkinter.Button(self.tk, text="8", font=self.sysfont);
        self.btn8.grid(row=3, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn9 = tkinter.Button(self.tk, text="9", font=self.sysfont);
        self.btn9.grid(row=3, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_minus = tkinter.Button(self.tk, text="-", font=self.sysfont);
        self.btn_minus.grid(row=3, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn0 = tkinter.Button(self.tk, text="0", font=self.sysfont);
        self.btn0.grid(row=4, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_point = tkinter.Button(self.tk, text=".", font=self.sysfont);
        self.btn_point.grid(row=4, column=1, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_es = tkinter.Button(self.tk, text="=", font=self.sysfont);
        self.btn_es.grid(row=4, column=2, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.btn_add = tkinter.Button(self.tk, text="+", font=self.sysfont);
        self.btn_add.grid(row=4, column=3, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E);

        self.tk.mainloop();

cal = Calculate();
