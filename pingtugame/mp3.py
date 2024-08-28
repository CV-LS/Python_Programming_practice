import pygame
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
pygame.mixer.init()
url = r"C:\Users\Dcnightmare\Desktop\Delacey - Dream It Possible.mp3"
# pygame.mixer.music.play(-1)
# time.sleep(10000)#如果要单个运行就必须使用这个，但是如果是运行在pygame程序中的就不需要，因为他有线程来运行
def load():
    pygame.mixer.music.load(url)
def start_listen():
    load()
    pygame.mixer.music.play(-1, 0)#-1表示循环播放，0表示从0开始
def stop_listen():
    pygame.mixer.music.stop()
