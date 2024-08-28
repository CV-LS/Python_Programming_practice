import os
import random
from tkinter import *
import pygame
import tkinter as tk
from PIL import Image, ImageTk

from renwu.pingtugame.Create_board import *
from renwu.pingtugame.Rule import *
from renwu.pingtugame.ShowPicture import *
from renwu.pingtugame.mp3 import *

'''判断游戏是否结束'''


counter=0#计时器

# 判断游戏是否结束
def isGameOver(board, size):
    assert isinstance(size, int )
    sum_chunk = size * size  # 总块数
    for i in range(sum_chunk - 1):  # 有一块需要丢去
        if board[i] != i: return False
    return True


'''随机选取一张图片'''


def GetImagePath(rootdir):
    imagenames = os.listdir(rootdir)
    assert len(imagenames) > 0
    return os.path.join(rootdir, random.choice(imagenames))


'''显示游戏结束界面'''

str_name = ''


def ShowEnd(screen, width, height, T):
    screen.fill(cfg.BACKGROUND)
    font = pygame.font.Font(cfg.FONTPATH, width // 15)
    if T:
        title = font.render('恭喜! 你共使用' + str(counter) + 's成功完成了拼图!', True, (233, 150, 122))
    else:
        title = font.render('抱歉! 你挑战失败', True, (233, 150, 122))
    ontent2 = font.render(r'继续游戏请点击S否则请点击E', True, cfg.BLUE)
    trect = ontent2.get_rect()
    trect.midtop = (width / 2, height / 10)
    rect = title.get_rect()
    rect.midtop = (width / 2, height / 2.5)
    screen.blit(title, rect)
    screen.blit(ontent2, trect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('s'):
                    return True
                if event.key == ord('e'):
                    return False
        pygame.display.update()


'''显示游戏开始界面'''


def ShowStart(screen, width, height):
    screen.fill(cfg.BACKGROUND)
    tfont = pygame.font.Font(cfg.FONTPATH, width // 4)
    cfont = pygame.font.Font(cfg.FONTPATH, width // 20)
    title = tfont.render('拼图游戏', True, cfg.RED)
    content1 = cfont.render('按H或M或L键开始游戏', True, cfg.BLUE)
    content2 = cfont.render(r'H为5*5模式-M为4*4模式-L为3*3模式', True, cfg.BLUE)
    trect = title.get_rect()  # 获取对象的属性，并修改
    trect.midtop = (width / 2, height / 10)
    # trect.midtop = (0, 100)#使用中间作为中心点
    crect1 = content1.get_rect()
    crect1.midtop = (width / 2, height / 2.2)
    crect2 = content2.get_rect()
    crect2.midtop = (width / 2, height / 1.8)
    screen.blit(title, trect)  # 对象，格式
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):#如果是shift+esc或者叉掉就直接结束
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('l'):
                    return 3
                elif event.key == ord('m'):
                    return 4
                elif event.key == ord('h'):
                    return 5
        pygame.display.update()  # pygame界面的刷新
image_path = ''
# 做项目时要多使用变量传参,主要好维护
def change_image():
    global image_path, flight
    flight = 0
    image_path = GetImagePath(cfg.PICTURE_ROOT_DIR)
    used_image = pygame.image.load(image_path)#加载图片
    used_image = pygame.transform.scale(used_image, (640,640))#为used_image设置长宽属性
    return used_image, used_image.get_rect()#image对象和他的属性


def create_button(screen, color, font_color, top, left, width, height, str):
    # pygame.draw.rect(screen, color, (top, left, width, height))#
    cfont1 = pygame.font.Font(cfg.FONTPATH, 25)
    picture = cfont1.render(str, True, font_color)  # 对象
    pic = picture.get_rect()  # 格式
    pic.topleft = (top + 1, left + 1)
    screen.blit(picture, pic)


flight = 0
challenge_time = 0
# # 导入构建数组
# from renwu.pingtugame.Create_board import *
# # 原图显示
# from renwu.pingtugame.ShowPicture import *
# # 规则说明
# from renwu.pingtugame.Rule import *
# # 添加背景音乐
# from renwu.pingtugame.mp3 import *
click_count = 0
def listen():
    global click_count
    if click_count % 2 == 0:
        start_listen()
    else:
        stop_listen()
    click_count += 1


'''主函数'''


def start():
    global flight, challenge_time, image_path,counter
    flight = 0  # 每次应该都是非挑战模式
    # 初始化
    pygame.init()
    clock = pygame.time.Clock()
    # 加载图片
    used_image, used_image_rect = change_image()
    # 设置窗口
    screen = pygame.display.set_mode((640, 690))
    pygame.display.set_caption('拼图游戏')
    # 游戏开始界面
    size = ShowStart(screen, 640, 640)
    rows, columns = size, size
    sum_chunk = size * size  # 块数
    # 计算Cell大小
    cell_width = 640 // columns
    cell_height = 640 // rows
    # 避免初始化为原图
    while True:
        board, index = CreateBoard(rows, columns, sum_chunk)
        if not isGameOver(board, size):
            break
    # 计数器
    counter = 0
    font = pygame.font.Font(cfg.FONTPATH, 26)
    time_ = font.render('用时: ' + str(counter) + 's', True, (0, 128, 0))
    mytimerevent = pygame.USEREVENT + 1
    pygame.time.set_timer(mytimerevent, 1000)#设置这个变量1s钟变化一次，并且mytimerevent变成了一个event对象
    counter_flag = 0  # 计数器标志位
    # 游戏主循环
    is_running = True
    while is_running:
        # --事件捕获
        for event in pygame.event.get():
            # ----退出游戏
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # ----键盘操作,实际都是在操作空白块，因为点击其他块的移动设计会比较复杂。从反面的角度来考虑并设计。
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    index = moveL(board, index, columns)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    index = moveR(board, index, columns)
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    index = moveU(board, index, rows, columns)
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    index = moveD(board, index, columns)
            # ----鼠标操作
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 20 <= x <= 70 and 650 <= y <= 680:
                    used_image, used_image_rect = change_image()
                    counter_flag = 0
                    counter = 0
                    time_ = font.render('用时: ' + str(counter) + 's', True, (0, 128, 0))
                    continue
                elif 90 <= x <= 140 and 650 <= y <= 680:
                    counter -= show_image(flight,image_path,counter_flag)
                    # thread2=myThread('thread')
                    # thread2.start()
                    # thread2.join()
                    continue
                elif 160 <= x <= 260 and 650 <= y <= 680 and flight == 0:
                    counter = 0
                    counter_flag = 0
                    time_ = font.render('用时: ' + str(counter) + 's', True, (0, 128, 0))
                    flight = 1
                    
                    if size == 3:
                        challenge_time = 30
                    elif size == 4:
                        challenge_time = 80
                    else:
                        challenge_time = 180
                elif 280 <= x <= 330 and 650 <= y <= 680:
                    counter_flag = 1
                elif 350 <= x <= 400 and 650 <= y <= 680:
                    pygame.quit()
                    start()
                elif 415 <= x <= 465 and 650 <= y <= 680:
                    listen()
                elif 480 <= x <= 530 and 650 <= y <= 680:
                    counter -= show_rules(counter_flag)  # 如果是非挑战时间是不会消耗时间的，但是如果是非挑战时间就会
                elif 0 <= x <= 640 and 0 <= y <= 640:  # 只能是在内部移动时才能开始计时，也视为游戏开始
                    counter_flag = 1

                x_pos = x // cell_width
                y_pos = y // cell_height
                idx = x_pos + y_pos * columns
                if idx == index - 1:
                    index = moveR(board, index, columns)
                elif idx == index + 1:
                    index = moveL(board, index, columns)
                elif idx == index + columns:
                    index = moveU(board, index, rows, columns)
                elif idx == index - columns:
                    index = moveD(board, index, columns)
            # 计数器
            if counter_flag == 1 and event.type == mytimerevent:  # timer event，时间对象，没有特殊情况，会每隔1s调用一次
                counter += 1
                time_ = font.render('用时: ' + str(counter) + 's', True, (0, 128, 0))
        # --判断游戏是否结束
        if index != sum_chunk - 1:
            pass
        elif isGameOver(board, size):
            board[index] = sum_chunk - 1
            is_running = False
        # --更新屏幕
        screen.fill(cfg.BACKGROUND)  # 初始化为白色
        create_button(screen, cfg.BACKGROUND, cfg.RED, 20, 650, 50, 30, '换图')  # 大量相同的按钮使用create_button函数封装
        create_button(screen, cfg.BACKGROUND, cfg.RED, 90, 650, 50, 30, '原图')
        create_button(screen, cfg.BACKGROUND, cfg.BLUE, 160, 650, 100, 30, '挑战模式')
        create_button(screen, cfg.BACKGROUND, (0, 206, 209), 280, 650, 50, 30, '开始')
        create_button(screen, cfg.BACKGROUND, (0, 206, 209), 350, 650, 50, 30, '退出')
        create_button(screen, cfg.BACKGROUND, (99, 99, 255), 415, 650, 50, 30, '音乐')
        create_button(screen, cfg.BACKGROUND, cfg.BLACK, 480, 650, 50, 30, '规则')
        time_rect = time_.get_rect()  # 获取对象的属性，并修改
        time_rect.topleft = (540, 650)
        screen.blit(time_, time_rect)
        for i in range(sum_chunk):
            if board[i] == -1:  # 为-1的位置就是空格位置（为背景色，白色），不需要进行着色
                continue
            x_pos = i // columns  # 空白着色，这是开始的位置，左上角x和y的坐标位置
            y_pos = i % columns
            rect = pygame.Rect(y_pos * cell_width, x_pos * cell_height, cell_width, cell_height)  # 放置格式(放置位置属性设置)
            img_area = pygame.Rect((board[i] % columns) * cell_width, (board[i] // columns) * cell_height,
                                   cell_width, cell_height)  # 取用格式
            screen.blit(used_image, rect, img_area)  # 使用的对象，格式，取用对象的某个位置（不使用整个对象，而是取一部分）实际也是格式
        #     为整个框划线
        for i in range(columns + 1):
            pygame.draw.line(screen, cfg.BLACK, (i * cell_width, 0), (i * cell_width, used_image_rect.height))
        for i in range(rows + 1):
            pygame.draw.line(screen, cfg.BLACK, (0, i * cell_height), (used_image_rect.width, i * cell_height))
        if flight and challenge_time <=counter:#只有一种失败情况
            if ShowEnd(screen, used_image_rect.width, used_image_rect.height, False) == False:
                del (screen)
                return
            else:
                start()
        pygame.display.update()  # 屏幕刷新
        # clock.tick(cfg.FPS)  # 刷新频率，如果是有动画，想要流畅的就可以使用clock.tick设置
    # 游戏结束界面
    if ShowEnd(screen, used_image_rect.width, used_image_rect.height, True) == False:
        del (screen)
    else:
        start()


import threading


class myThread(threading.Thread):  # 多线程只能保障并发执行，并不能保证并行执行。进程才能并行执行
    def __init__(self, str):
        threading.Thread.__init__(self)
        self.str = str

    def run(self):
        if self.str == 'main':
            start()


'''run'''
if __name__ == '__main__':
    thread1 = myThread('main')
    thread1.start()
    thread1.join()
