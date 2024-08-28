from tkinter import *
from math import pi
from math import e
import tkinter as tk
# 能否类似于海龟画图中的有范围点击触发函数，这样就可以实现类似于带背景的计算器，界面->可以使用画布创建对象即可

win = Tk()
win.title('计算器')
win.geometry('693x700')
win.resizable(width=False, height=False)
# canvas = tk.Canvas(win, width=700, height=700, bd=0, highlightthickness=0)#如果需要背景图就要加上画布
# canvas.configure(bg='write')
en = Entry(win, width=70, font=('Microsoft YaHei', 20), highlightcolor='Magenta4', relief='groove',
               xscrollcommand=True, bd=3)

#导入基本函数
ans = 0.0
flag = 0
falg = 0

instack = {'+': 1, '-': 1, '*': 3, '/': 3, '%': 3, '(': 6, ')': 0}
putstack = {'+': 2, '-': 2, '*': 4, '/': 4, '%': 4, '(': 0, ')': 7}
#非动态获取数据，使用的是触发式获取
def calculator(str1):
    try:
        data_list = []
        yunsuan_list = []
        i = 0
        while i != len(str1):
            if str.isdigit(str1[i]):
                for k in range(i, len(str1)):
                    if str1[k] == 'e':
                        if str1[k + 1] == '-':
                            falg=0
                            p=k+2
                            for j in range(k + 2, len(str1)):
                                if str1[j]=='0' and falg==0:
                                    continue
                                elif str.isdigit(str1[j]) and falg==0:
                                        p=j
                                        falg=1
                                if str.isdigit(str1[j]) == 0:
                                    data_list.append(eval(str1[i:k]) * 10 ** (eval('-' + str1[p:j])))
                                    i = j
                                    break
                                if j == len(str1) - 1:
                                    data_list.append(eval(str1[i:k]) * 10 ** (eval('-' + str1[p:j + 1])))
                                    i = j + 1
                                    break
                        break
                    if str.isdigit(str1[k]) == 0 and str1[k] != '.':
                        data_list.append(eval(str1[i:k]))
                        i = k
                        break
                    if k == len(str1) - 1:
                        data_list.append(eval(str1[i:k + 1]))
                        i = k + 1
                        break
            else:
                # print(str1[i])
                if (str1[i] == '-' or str1[i] == '+') and str.isdigit(str1[i + 1]) and (i == 0 or str1[i - 1] == '('):#这里我们可以使用-但是为了区别普通的减法所以我们
                    #使用（将其括上）
                    for k in range(i + 1, len(str1)):
                        if str.isdigit(str1[k]) == 0 and str1[k] != '.':
                            data_list.append(eval(str1[i:k]))
                            # Function_Ansstr1 += str(eval(str1[i:k])) + ' '
                            i = k
                            break
                        if k == len(str1) - 1:
                            # print('ok')
                            data_list.append(eval(str1[i:k + 1]))
                            # Function_Ansstr1 += str(eval(str1[i:k + 1])) + ' '
                            i = k + 1
                            break
                else:
                    while len(yunsuan_list) != 0 and putstack[yunsuan_list[-1]] > instack[str1[i]]:
                        l = data_list[-1]
                        data_list.pop()
                        r = data_list[-1]
                        data_list.pop()
                        data_list.append(eval(str(r) + yunsuan_list[-1] + str(l)))
                        # Function_Ansstr1 += yunsuan_list[-1] + ' '
                        yunsuan_list.pop()
                    if str1[i] != ')':
                        yunsuan_list.append(str1[i])
                    elif len(yunsuan_list) != 0 and yunsuan_list[-1] == '(':
                        yunsuan_list.pop()
                    i += 1
        while len(yunsuan_list):
            l = data_list[-1]
            data_list.pop()
            r = data_list[-1]
            data_list.pop()
            data_list.append(eval(str(r) + yunsuan_list[-1] + str(l)))
            # Function_Ansstr1 += yunsuan_list[-1] + ' '
            yunsuan_list.pop()
        if data_list[-1] == int(data_list[-1]):
            return int(data_list[-1])
        else:
            return data_list[-1]
    except Exception:
        en.delete(0,'Error')
    # finally:
    #     if flag1==0:
    #         en.delete(0, END)
    #         en.insert(0, '错误')
    #         flag1=1

def Function_Two():#二元运算
    try:
        num = str(en.get())
        for i in range(0, len(num)):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                number = eval(num[0:i])
                en.delete(0, END)
                if num[i] == '^':
                    en.insert(0, str(number ** (calculator(num[i + 1:]))))
                else:
                    en.insert(0, str(number * (10 ** calculator(num[i + 3:]))))
                return
    except Exception:
        en.delete(0, END)
        en.insert(0, 'Error')

def Function_PutNum(number):
    try:
        global flag
        if (flag):
            en.delete(0, END)
            flag = 0
        first_num = en.get()
        en.delete(0, END)
        if first_num == 'Error':
            en.insert(0, str(number))
            return
        # print(first_num)
        en.insert(0, str(first_num) + str(number))
    except Exception:
        en.delete(0, END)
        en.insert(0, 'Error')

def clear():
    en.delete(0, END)


def Function_DelAll():
    en.delete(len(str(en.get())) - 1, END)


def Function_1_x():
    try:
        num = str(en.get())
        n = 1
        # if(num[-1]==')'):#如果想要整体做1/x可以使用加括号的方法
        #         en.delete(0,END)
        #         en.insert(0,str(1/eval(num[1:-2])))
        #         return
        if (num[-1] == ')'):
            for i in range(len(num) - 2, 0, -1):
                if (num[i] == ')'):
                    n += 1
                elif num[i] == '(':
                    n -= 1
                if (n == 0):
                    en.delete(0, END)
                    # print(num[i+1:-2])
                    en.insert(0, num[0:i] + str(1 / calculator(num[i + 1:-1])))
                    # 注意切片也是满足左开右闭的情况，只有右侧不取数字时才有
                    # 可以得到从对应位置到最后的结果
                    return

        for i in range(len(num) - 1, 0, -1):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                pp = float(num[i + 1:])
                if pp == 0:
                    en.delete(0, END)
                    en.insert('Error')
                # print('ok')
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(1 / pp))
                return
        en.delete(0, END)
        en.insert(0, str(1 / float(num[0:])))
    except Exception:
        en.delete(0, END)
        en.insert(0, 'Error')

def Function_Power():#幂
    try:
        num = str(en.get())
        for i in range(len(num) - 1, 0, -1):  # 只需要读到第二个字符即可，因为如果第二个字符都不是字符
            # 则即使前面是字符也是属于单目符号(这里只有  自取负符号-）对结果无关紧要
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(calculator(num[i:]) * calculator(num[i:])))
                return
        en.delete(0, END)
        en.insert(0, str(calculator(num) * calculator(num)))
    except Exception:
        en.insert(0, 'Error')

# 当点了=之后如果第一个为数字则就可以重新开始若要使用之前的数据可以使用ans
# 但是如果是使用的符号则需要使用之前的数字不做修改
def Function_Add(x):
    global falg
    if (x == 'exp' or x == '^'):
        falg = 1
    num = en.get()
    en.delete(0, END)
    global flag
    if (flag):
        en.insert(0, str(ans) + x)
        flag = 0
    else:
        en.insert(0, str(num) + x)


def Function_eq():
    try:
        global ans
        global flag
        global falg
        # for i in str(en.get()):
        if falg:
            Function_Two()  # 主要用于特殊的二元运算符如^ 和 exp
            falg = 0
            return
        num = calculator(str(en.get()))
        en.delete(0, END)
        en.insert(0, str(num))
        ans = num
        flag = 1
    except Exception:
        en.delete(0,END)
        en.insert(0, 'Error')


def Function_Ans():
    global ans
    num = en.get()
    en.delete(0, END)
    en.insert(0, str(num) + str(ans))


def Function_Abs():
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        en.delete(0, END)
        en.insert(0, str(abs(calculator(num))))
    except Exception:
        en.insert(0, 'Error')

def Function_factorial():#阶乘
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        en.delete(0, END)
        sum = 1
        k = abs(calculator(num))
        for i in range(2, k + 1, 1):
            sum *= i
        en.insert(0, str(sum))
    except Exception:
        en.insert(0, 'Error')

def Function_Sqrt():
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        for i in range(len(num) - 1, 0, -1):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(math.sqrt(calculator(num[i + 1:]))))
                return
        en.delete(0, END)
        if eval(num[0:]) < 0:
            en.insert(0, 'Error')
            return
        en.insert(0, str(math.sqrt(calculator(num))))
    except Exception:
        en.insert(0, 'Error')

def Function_Mark():
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        for i in range(len(num) - 1, 0, -1):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(10 ** (calculator(num[i + 1:]))))
                return
        en.delete(0, END)
        en.insert(0, str(10 ** (calculator(num))))
    except Exception:
        en.insert(0, 'Error')

def fu():
    try:
        num = en.get()
        if num == '':
            en.insert(0, 'Error')
            return
        en.delete(0, END)
        en.insert(0, '-' + str(num))
    except Exception:
        en.insert(0, 'Error')

def Function_Iog():
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        for i in range(len(num) - 1, 0, -1):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(math.log10(calculator(num[i + 1:]))))
                return
        en.delete(0, END)
        if eval(num[0:]) <= 0:
            en.insert(0, 'Error')
            return
        en.insert(0, str(math.log10(calculator(num[0:]))))
    except Exception:
        en.insert(0, 'Error')

def Function_In():
    try:
        num = str(en.get())
        if num == '':
            en.insert(0, 'Error')
            return
        for i in range(len(num) - 1, 0, -1):
            if (str.isdigit(num[i]) or num[i] == '.') == 0:
                en.delete(0, END)
                en.insert(0, num[0:i + 1] + str(math.log(calculator(num[i + 1:]))))
                return
        en.delete(0, END)
        if eval(num[0:]) <= 0:
            en.insert(0, 'Error')
            return
        en.insert(0, str(math.log(calculator(num[0:]))))
    except Exception:
        en.insert(0, 'Error')

but7= Button(win,text=7,width=5,font=('Arial',31),command=lambda :Function_PutNum(7),activeforeground='blue',foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but8= Button(win,text=8,width=5,font=('Arial',31),command=lambda :Function_PutNum(8),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but9=Button(win,text=9,width=5,font=('Arial',31),command=lambda :Function_PutNum(9),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but4=Button(win,text=4,width=5,font=('Arial',31),command=lambda :Function_PutNum(4),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but5=Button(win,text=5,width=5,font=('Arial',31),command=lambda :Function_PutNum(5),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but6=Button(win,text=6,width=5,font=('Arial',31),command=lambda :Function_PutNum(6),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but1=Button(win,text=1,width=5,font=('Arial',31),command=lambda :Function_PutNum(1),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but2=Button(win,text=2,width=5,font=('Arial',31),command=lambda :Function_PutNum(2),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but3= Button(win,text=3,width=5,font=('Arial',31),command=lambda :Function_PutNum(3),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
but0=Button(win,text=0,width=5,font=('Arial',31),command=lambda :Function_PutNum(0),activeforeground='blue', foreground='Turquoise2',relief=tk.SOLID,cursor='dotbox')
bu1=Button(win,text='ans',width=5,font=('Arial',31),command=Function_Ans,activeforeground='yellow', foreground='black',relief=tk.RIDGE,cursor='dotbox')
bu2=Button(win,text='π',width=5,font=('Arial',31),command=lambda :Function_PutNum(pi),activeforeground='yellow', foreground='DarkSlateGray',relief=tk.RIDGE,cursor='dotbox')
bu3= Button(win,text='e',width=5,font=('Arial',31),command=lambda :Function_PutNum(e),activeforeground='yellow', foreground='DarkSlateGray',relief=tk.RIDGE,cursor='dotbox')
bu4=Button(win,text='CE',width=5,font=('Arial',31),command=clear,activeforeground='red', foreground='Red',relief=tk.RIDGE,cursor='dotbox')
bu5=Button(win,text='del',width=5,font=('Arial',31),command=Function_DelAll,activeforeground='red', foreground='Red',relief=tk.RIDGE,cursor='dotbox')
bu6=Button(win,text='x^2',width=5,font=('Arial',31),command=Function_Power,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
bu7=Button(win,text='1/x',width=5,font=('Arial',31),command=Function_1_x,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
bu8=Button(win,text='|x|',width=5,font=('Arial',31),command=Function_Abs,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
bu9=Button(win,text='exp',width=5,font=('Arial',31),command=lambda :Function_Add('exp'),activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
bu0=Button(win,text='mod',width=5,font=('Arial',31),command=lambda:Function_Add('%'),activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b1=Button(win,text='sqrt()',width=5,font=('Arial',31),command=Function_Sqrt,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b2=Button(win,text='(',width=5,font=('Arial',31),command=lambda :Function_Add('('),activeforeground='purple', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b3=Button(win,text=')',width=5,font=('Arial',31),command=lambda :Function_Add(')'),activeforeground='purple', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b4=Button(win,text='n!',width=5,font=('Arial',31),command=Function_factorial,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b5=Button(win,text='/',width=5,font=('Arial',31),command=lambda :Function_Add('/'),activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b6=Button(win,text='x^y',width=5,font=('Arial',31),command=lambda :Function_Add('^'),activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b7=Button(win,text='*',width=5,font=('Arial',31),command=lambda :Function_Add('*'),activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b8=Button(win,text='10^x',width=5,font=('Arial',31),command=Function_Mark,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b9=Button(win,text='-',width=5,font=('Arial',31),command=lambda :Function_Add('-'),activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b0=Button(win,text='log',width=5,font=('Arial',31),command=Function_Iog,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b11=Button(win,text='+',width=5,font=('Arial',31),command=lambda :Function_Add('+'),activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b12=Button(win,text='ln',width=5,font=('Arial',31),command=Function_In,activeforeground='red', foreground='MediumBlue',relief=tk.RIDGE,cursor='dotbox')
b13=Button(win,text='+/-',width=5,font=('Arial',31),command=fu,activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b14=Button(win,text='.',width=5,font=('Arial',31),command=lambda :Function_Add('.'),activeforeground='red', foreground='Orange1',relief=tk.RIDGE,cursor='dotbox')
b15 = Button(win,text='=',width=5,font=('Arial',31),command=Function_eq,activeforeground='red', foreground='Green',relief=tk.RIDGE,cursor='dotbox')

#功能扩展区

#1.查询汇率
from renwu.catulator.huilv import *
def huilv():
    HuiLv()
#2.贷款计算
from renwu.catulator.daikuan import *
def Daikuan():
    DaiKuan()
#3.连接校园网和选课
from renwu.catulator.xuanke import *
#4.三角函数
from renwu.catulator.rectangle import *
def rec():
    Rec()
#5.密码库
from renwu.catulator.mysql import *
def password():
    Mysql()

def place_button():
    b6.place(x=0, y=340)
    but7.place(x=140, y=340)
    but8.place(x=280, y=340)
    but9.place(x=420, y=340)
    b7.place(x=560, y=340)

    b8.place(x=0, y=430)
    but4.place(x=140, y=430)
    but5.place(x=280, y=430)
    but6.place(x=420, y=430)
    b9.place(x=560, y=430)

    b0.place(x=0, y=520)
    but1.place(x=140, y=520)
    but2.place(x=280, y=520)
    but3.place(x=420, y=520)
    b11.place(x=560, y=520)

    b12.place(x=0, y=610)
    b13.place(x=140, y=610)
    but0.place(x=280, y=610)
    b14.place(x=420, y=610)
    b15.place(x=560, y=610)

    bu1.place(x=0, y=71)
    bu2.place(x=140, y=71)
    bu3.place(x=280, y=71)
    bu4.place(x=420, y=71)
    bu5.place(x=560, y=71)

    bu6.place(x=0, y=160)
    bu7.place(x=140, y=160)
    bu8.place(x=280, y=160)
    bu9.place(x=420, y=160)
    bu0.place(x=560, y=160)

    b1.place(x=0, y=250)
    b2.place(x=140, y=250)
    b3.place(x=280, y=250)
    b4.place(x=420, y=250)
    b5.place(x=560, y=250)
    en.place(x=0, y=0)
    opp = Button(win, text='汇率', bg='lavender', command=huilv, highlightcolor='Magenta4', relief=tk.RIDGE)
    opp.place(x=0, y=41)
    dai=Button(win,text="贷款计算",bg="lavender",command=Daikuan,highlightcolor='Magenta4',relief=tk.RIDGE)
    dai.place(x=140,y=41)
    # wife = Button(win, text="连接校园网", bg="lavender", command=get_wife, highlightcolor='Magenta4', relief=tk.RIDGE)
    # wife.place(x=420, y=41)
    # wife = Button(win, text="抢课", bg="lavender", command=xuanke, highlightcolor='Magenta4', relief=tk.RIDGE)
    # wife.place(x=655, y=41)
    rect=Button(win, text="三角函数", bg="lavender", command=rec, highlightcolor='Magenta4', relief=tk.RIDGE)
    rect.place(x=280, y=41)
    mysql = Button(win, text="密码库", bg="lavender", command=password, highlightcolor='Magenta4', relief=tk.RIDGE)
    mysql.place(x=560, y=41)
place_button()
# canvas.pack()
mainloop()


