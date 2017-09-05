#! /usr/bin/python3.5
from tkinter import *

root = Tk()  # 用库中的 Tk() 方法创建主窗口，并把窗口名称赋值给 root
root.title("The title of this window ")


def show():
    print("作品：<<%s>>" % e1.get())
    print("作者：%s" % e2.get())
    text.delete(1.0, END)
    text.insert(INSERT, "作品：" + e1.get())
    text.insert(INSERT, "\n作者：" + e2.get())

    e1.delete(0, END)
    e2.delete(0, END)


frame = Frame(root)
frame.pack(padx=50, pady=40)  # set area
label = Label(frame, text="作品：", font=("华康少女字体", 15), fg="blue").grid(row=0, column=0, padx=15, pady=5)
label = Label(frame, text="作者：", font=("华康少女字体", 15), fg="red").grid(row=1, column=0, padx=15, pady=5)

e1 = Entry(frame, foreground='blue', font=('Helvetica', '12'))
e2 = Entry(frame, font=('Helvetica', '12', 'bold'))
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
hi_there = Button(frame, text=" 读取信息 ", font=("宋体", 15), width=10, command=show).grid(row=2, column=0, padx=15, pady=5)
hi_there = Button(frame, text=" 退出 ", font=("宋体", 15), width=10, command=root.quit).grid(row=2, column=1, padx=15,
                                                                                         pady=5)
# self.hi_there.pack()
text = Text(frame, width=30, height=6, font=("华康少女字体", 15))
text.grid(row=3, column=0, padx=35, pady=5, columnspan=2)

root.mainloop()
