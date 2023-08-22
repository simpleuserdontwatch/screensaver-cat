from tkinter import *
import time
from PIL import ImageTk,Image
import os
root = Tk()
root.wm_attributes("-fullscreen",True)
frameCnt = 76
w,h= root.winfo_screenwidth(),root.winfo_screenheight()
frames = [ImageTk.PhotoImage(Image.open(f'frames/f ({str(i)}).jpg').resize((w,h)))for i in range(1,frameCnt+1)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
root.bind("<Motion>", lambda event: root.destroy())
label = Label(root,mouse="none")
label.pack()
root.after(0, update, 0)
root.mainloop()