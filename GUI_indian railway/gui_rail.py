from tkinter import * 
from PIL import Image , ImageTk 
import os
import pygame
import cv2
import pandas as pd

SET_WIDTH = 650
SET_HEIGHT = 368
global x
x = 0
pygame.mixer.init()

class LetterButtons:

    def __init__(self, master):
        self.master = master
        df = pd.read_excel('announce.xls')
        nums = df['train_no']
        for l in nums:
            self.button = Button(self.master, text=l + ' Hindi', bg='orange', width=50)
            self.button['command'] = lambda idx=l, binst=self.button: self.click('hin', binst, idx)
            self.button.pack()
            self.button = Button(self.master, text=l + ' English', bg='orange', width=50)
            self.button['command'] = lambda idx=l, binst=self.button: self.click('eng', binst, idx)
            self.button.pack()

    def click(self, lang, binst, idx):
        if lang == 'hin':
            os.chdir('C:\\Users\\Deepanshu\\Desktop\\python\\GUI_indian railway\\Hindi')
        else:
            os.chdir('C:\\Users\\Deepanshu\\Desktop\\python\\GUI_indian railway\\English')
        ls=os.listdir()
        for l in ls:
            if idx in l: 
                pygame.mixer.music.load(l)
                pygame.mixer.music.play()
        os.chdir('C:\\Users\\Deepanshu\\Desktop\\python\\GUI_indian railway')
        binst.destroy()


window = Tk()
window.title("Indian Railway announcement System")
cv_img = cv2.cvtColor(cv2.imread("download.png"), cv2.COLOR_BGR2RGB)
canvas = Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=NW, image=photo)
canvas.pack()

lett = LetterButtons(window)

window.mainloop()
