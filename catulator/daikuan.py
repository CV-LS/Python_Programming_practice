from  tkinter import *
class DaiKuan:
    def __init__(self):
        self.daikuan()
    def daikuan(self):
        win1 = Toplevel()  # 建立窗口,如果只是使用已有数据不需输入，可以直接使用tk窗口。但是如果需要使用到子窗口的数据输入就必须用到toplevel.(与主线程共用一个资源，可以来回切换）
        #区别pygame，pygame是不能共享资源的，也不支持来回切换，只能串行执行。所以在一个时刻只能有一个打开。而tk同时可打开多个，可以随时使用其中任何一个（并发执行）。

        win1.title("贷款计算器")  # 命名窗口标题

        # 定义StringVar对象动态存储输入框的值
        self.amountVar = StringVar()  # 贷款金额
        self.rateVar = StringVar()  # 年化利率
        self.yearsVar = StringVar()  # 贷款年限
        self.monthsVar = StringVar()  # 已还期数
        self.monthVar = StringVar()  # 第i月

        self.total_1Var = StringVar()  # 等额本息总还款额
        self.totalInterest_1Var = StringVar()  # 等额本息总利息
        self.total_Repaied_1Var = StringVar()  # 等额本息累计已还
        self.remain_1Var = StringVar()  # 等额本息待还金额
        self.month_Repay_1Var = StringVar()  # 等额本息第i月应还

        self.total_2Var = StringVar()  # 等额本金总还款额
        self.totalInterest_2Var = StringVar()  # 等额本金总利息
        self.total_Repaied_2Var = StringVar()  # 等额本金累计已还
        self.remain_2Var = StringVar()  # 等额本金待还金额
        self.month_Repay_2Var = StringVar()  # 等额本金第i月应还

        # 设置一些默认值
        self.monthsVar.set("0")
        self.monthVar.set('1')

        # 整体面板，设置总体的边距
        frame = Frame(win1)
        frame.pack(padx=20, pady=20)

        """
        添加标签
        .grid(row, column)设置标签位置
        """
        Label(frame, text="贷款金额").grid(row=1, column=1, columnspan=3)#columnspan用于将元素跨越多少列，row和column用于设置元素放置位置（中心位置）
        Label(frame, text="年化利率").grid(row=2, column=1, columnspan=3)
        Label(frame, text="贷款年限").grid(row=3, column=1, columnspan=3)
        Label(frame, text="已还期数").grid(row=4, column=1, columnspan=3)
        Label(frame, text="总还款额").grid(row=7, column=1, columnspan=3)
        Label(frame, text="总利息额").grid(row=8, column=1, columnspan=3)
        Label(frame, text="累计已还").grid(row=9, column=1, columnspan=3)
        Label(frame, text="剩余待还").grid(row=10, column=1, columnspan=3)
        Label(frame, text="第").grid(row=11, column=1)
        Label(frame, text="月应还").grid(row=11, column=3)

        """
        添加输入和输出框
        textvariable = self.amountVar 由相应的StringVar对象动态保存输入框中的文本
        justify=RIGHT 输入框中的文本右对齐
        sticky=E 控件在单元格中右对齐
        """
        Entry(frame, justify=RIGHT, textvariable=self.amountVar).grid(row=1, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.rateVar).grid(row=2, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.yearsVar).grid(row=3, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.monthsVar).grid(row=4, column=4)
        Entry(frame, width=4, justify=CENTER, textvariable=self.monthVar).grid(row=11, column=2)
        Label(frame, textvariable=self.total_1Var).grid(row=7, column=4, sticky=E)
        Label(frame, textvariable=self.total_2Var).grid(row=7, column=6, sticky=E)
        Label(frame, textvariable=self.totalInterest_1Var).grid(row=8, column=4, sticky=E)
        Label(frame, textvariable=self.totalInterest_2Var).grid(row=8, column=6, sticky=E)
        Label(frame, textvariable=self.total_Repaied_1Var).grid(row=9, column=4, sticky=E)
        Label(frame, textvariable=self.total_Repaied_2Var).grid(row=9, column=6, sticky=E)
        Label(frame, textvariable=self.remain_1Var).grid(row=10, column=4, sticky=E)
        Label(frame, textvariable=self.remain_2Var).grid(row=10, column=6, sticky=E)
        Label(frame, textvariable=self.month_Repay_1Var).grid(row=11, column=4, sticky=E)
        Label(frame, textvariable=self.month_Repay_2Var).grid(row=11, column=6, sticky=E)

        # 添加Message存储单位
        Message(frame, text="元").grid(row=1, column=5)
        Message(frame, text="%").grid(row=2, column=5)
        Message(frame, text="年").grid(row=3, column=5)
        Message(frame, text="月").grid(row=4, column=5)
        Message(frame, text="元").grid(row=7, column=5)
        Message(frame, text="元").grid(row=7, column=7)
        Message(frame, text="元").grid(row=8, column=5)
        Message(frame, text="元").grid(row=8, column=7)
        Message(frame, text="元").grid(row=9, column=5)
        Message(frame, text="元").grid(row=9, column=7)
        Message(frame, text="元").grid(row=10, column=5)
        Message(frame, text="元").grid(row=10, column=7)
        Message(frame, text="元").grid(row=11, column=5)
        Message(frame, text="元").grid(row=11, column=7)

        # 空Frame以撑开空间
        Frame(frame, height=10).grid(row=5, column=4, columnspan=7)


        # 按钮，事件监听函数为calculate
        Button(frame, width=19, text="等额本息", command=self.calculate_1).grid(row=6, column=4, columnspan=1, pady=0)#columnspan用于控制跨越多少行,pady用于控制与y轴的距离
        Button(frame, width=19, text="等额本金", command=self.calculate_2).grid(row=6, column=6, columnspan=1, pady=0)

        # 消息循环
        win1.mainloop()
  # 按钮点击监听
    def calculate_1(self):
        """
        等额本息法计算函数
        """
        # 获取输入的参数
        amount = eval(self.amountVar.get())
        rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
        years = eval(self.yearsVar.get())
        months = eval(self.monthsVar.get())
        month = eval(self.monthVar.get())

        # 计算每月还款
        month_Repay = amount * rate * ((1 + rate) ** (years * 12)) / ((1 + rate) ** (years * 12) - 1)

        # 将计算结果设置给控件
        total = month_Repay * 12 * years  # 总还款金额
        self.total_1Var.set(format(total, ".3f"))

        totalInterest = total - amount  # 总利息
        self.totalInterest_1Var.set(format(totalInterest, '.3f'))

        if (months >= 0) and (months <= years * 12):  # 已还期数必须在贷款期数内
            total_Repaied = month_Repay * months  # 已还金额
            remain = total - total_Repaied  # 剩余待还金额
            self.total_Repaied_1Var.set(format(total_Repaied, '.3f'))
            self.remain_1Var.set(format(remain, '.3f'))
        else:
            self.total_Repaied_1Var.set('已还期数输入有误!')
            self.remain_1Var.set('已还期数输入有误!')

        if (month >= 1) and (month <= years * 12):
            self.month_Repay_1Var.set(format(month_Repay, '.3f'))
        else:
            self.month_Repay_1Var.set('第_月份输入有误!')

    def calculate_2(self):
        """
        等额本金法计算函数
        """
        # 获取输入的参数
        amount = eval(self.amountVar.get())
        rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
        years = eval(self.yearsVar.get())
        months = eval(self.monthsVar.get())
        month = eval(self.monthVar.get())
        month_amount = amount / (years * 12)
        # 存储每月还款
        month_Repay = []
        for i in range(1, (years * 12) + 1):
            monthpayment = month_amount + (amount - (i - 1) * month_amount) * rate
            month_Repay.append(monthpayment)
        # 将计算结果设置给控件
        total = sum(month_Repay)
        self.total_2Var.set(format(total, ".3f"))
        totalInterest = total - amount
        self.totalInterest_2Var.set(format(totalInterest, '.3f'))
        if (months >= 0) and (months <= years * 12):
            total_Repaied = sum(month_Repay[:months])
            remain = total - total_Repaied
            self.total_Repaied_2Var.set(format(total_Repaied, '.3f'))
            self.remain_2Var.set(format(remain, '.3f'))
        else:
            self.total_Repaied_2Var.set('已还期数输入有误!')
            self.remain_2Var.set('已还期数输入有误!')

        if (month >= 1) and (month <= years * 12):
            self.month_Repay_2Var.set(format(month_Repay[month - 1], '.3f'))
        else:
            self.month_Repay_2Var.set('第_月份输入有误!')

