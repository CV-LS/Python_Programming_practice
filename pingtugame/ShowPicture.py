import time
import tkinter as tk
from PIL import ImageTk,Image
def show_image(flight,image_path,counter_flag):
    if flight == 0 and counter_flag == 1:
        start_time = int(time.time())
    else:
        start_time = 0
    win=tk.Tk()
    win.geometry('640x640')
    win.title("原图")
    img = Image.open(image_path)
    img = img.resize((640, 640))
    photo = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(win, height=640, width=640)
    canvas.create_image(320,320,image=photo)
    canvas.pack()
    win.mainloop()
    if start_time == 0:
        return 0
    return int(time.time()) - start_time-1


