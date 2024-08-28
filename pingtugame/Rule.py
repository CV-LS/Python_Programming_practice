import time
import tkinter as tk
from renwu.pingtugame.pingtu_end import flight


def show_rules(counter_flag):
    if flight==0 and counter_flag==1:
        start_time=int(time.time())
    else:
        start_time=0
    win = tk.Tk()
    # win.geometry('640x640')
    win.title('游戏规则')
    frame = tk.Frame(win)
    frame.pack(padx=30, pady=30)
    tk.Label(frame, text="拼图游戏规则", font = 'Helvetica -30 bold').grid(row=0, column=1, columnspan=3)
    tk.Label(frame, text="1.玩家通过使用开始按钮或者直接移动游戏区方块开始游戏并计时").grid(row=2, column=0, columnspan=3,sticky='w')
    tk.Label(frame, text="2.玩家可使用挑战模式按钮开启挑战，游戏会根据当前难度设置时间，难度低到高通过时间分别为30s,80s,180s").grid(row=3, column=1, columnspan=3,sticky='w')
    tk.Label(frame, text="3.玩家在挑战模式过程中不能暂停和重新开始，如果想要退出可以点击退出按钮重新开始或者关闭窗口").grid(row=4, column=1, columnspan=3,sticky='w')
    tk.Label(frame, text="4.玩家在非挑战模式下查看原图和查看规则都不会计入时间，但是在挑战模式下，如何操作都将计入时间").grid(row=5, column=1, columnspan=3,sticky='w')
    tk.Label(frame, text="5.玩家可以随时打开或者关闭音乐，用法是点击一次打开，点击两次关闭").grid(row=6, column=1, columnspan=3,sticky='w')
    tk.Frame(frame, height=10).grid(row=6, column=4, columnspan=7)
    win.mainloop()
    if start_time==0:
        return 0
    return int(time.time())-start_time-1