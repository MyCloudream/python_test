from tkinter import *
# messagebox : 消息对话框
import tkinter.messagebox


# 定义一个类，一般也可以继承自Frame
class MainWindow:
    # 按钮监听方法
    def buttonListener1(self, event):
        # 弹出对话框
        tkinter.messagebox.showinfo("messagebox", "this is button 1 dialog")

    def buttonListener2(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 2 dialog")

    def buttonListener3(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 3 dialog")

    def buttonListener4(self, event):
        tkinter.messagebox.showinfo("messagebox", "this is button 4 dialog")

    # 相当于构造方法，这里的self相当类似Java中的this
    def __init__(self):
        # 实例化主窗体
        self.frame = Tk()
        # 定义4个按钮
        self.button1 = Button(self.frame, text="button1", width=10, height=5)
        self.button2 = Button(self.frame, text="button2", width=10, height=5)
        self.button3 = Button(self.frame, text="button3", width=10, height=5)
        self.button4 = Button(self.frame, text="button4", width=10, height=5)
        # 设定4个按钮，按照grid()方式管理，其实就是网状布局，指定行列坐标，指定x、y轴上的间隙
        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3.grid(row=1, column=0, padx=5, pady=5)
        self.button4.grid(row=1, column=1, padx=5, pady=5)
        # 给按钮绑定事件，第一个参数表示事件的类型，为固定值，第二个参数为触发事件时调用的方法
        self.button1.bind("<ButtonRelease-1>", self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>", self.buttonListener2)
        self.button3.bind("<Leave>", self.buttonListener3)
        self.button4.bind("<Double-ButtonRelease-1>", self.buttonListener4)
        self.frame.mainloop()


window = MainWindow()