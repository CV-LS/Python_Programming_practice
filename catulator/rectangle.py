from tkinter import *
import math
from sympy import *


class Rec:
    def __init__(self):
        self.string = ""
        win2 = Toplevel()
        win2.title("三角函数")
        # self.text = StringVar()#直接使用stringvar作为接收变量，就不需要delete和insert=>多用于窗口按键时使用，方便改变entry值，或者可变标签使用
        self.sin = StringVar()  # 贷款金额
        self.cos = StringVar()  # 年化利率
        self.tan = StringVar()  # 贷款年限
        self.cot = StringVar()  # 已还期数
        self.sec = StringVar()  # 第i月
        self.csc = StringVar()  # 等额本息总还款额
        frame = Frame(win2)
        frame.pack(padx=20, pady=20)#设置窗口框与外框间距

        self.text=Entry(frame, justify=RIGHT)
        self.text.grid(row=1, column=4)
        Button(frame, width=10, text="start", command=self.calculate).grid(row=1, column=6, columnspan=1, pady=0)
        Label(frame, text="角度值:").grid(row=1, column=1, columnspan=3)
        Label(frame, text="sin:").grid(row=2, column=1, columnspan=3)
        Label(frame, text="cos:").grid(row=3, column=1, columnspan=3)
        Label(frame, text="tan:").grid(row=4, column=1, columnspan=3)
        Label(frame, text="cot:").grid(row=5, column=1, columnspan=3)
        Label(frame, text="sec:").grid(row=6, column=1, columnspan=3)
        Label(frame, text="csc:").grid(row=7, column=1, columnspan=3)
        Label(frame, textvariable=self.sin).grid(row=2, column=4, sticky=E)  # eval不能为空字符    [self.text.get(),"0"][self.text.get()!=""]
        Label(frame, textvariable=self.cos).grid(row=3, column=4, sticky=E)
        Label(frame, textvariable=self.tan).grid(row=4, column=4, sticky=E)
        Label(frame, textvariable=self.cot).grid(row=5, column=4, sticky=E)
        Label(frame, textvariable=self.sec).grid(row=6, column=4, sticky=E)
        Label(frame, textvariable=self.csc).grid(row=7, column=4, sticky=E)
        win2.mainloop()

    def calculate(self):
        if self.string == self.text.get():#如果重复就不需要再计算
            return
        if self.text.get() == "":
            # self.text="0"
            self.text.set("0")
        self.string=self.text.get()#保留上次的结果
        mid =getdouble(eval(self.text.get()))
        self.sin.set(math.sin(math.radians(mid)))
        self.cos.set(math.cos(math.radians(mid)))
        self.tan.set(math.tan(math.radians(mid)))
        self.cot.set(cot(math.radians(mid)))
        self.sec.set(sec(math.radians(mid)))
        self.csc.set(csc(math.radians(mid)))


