#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import os
import tkFileDialog as filedialog
from PIL import Image
window = Tk()
window.geometry('512x200')
window.title('pyImage Compressor by Himanshu Nag')


def clicked():
    file = filedialog.askopenfilename(filetypes=(('Image files',
            '*.jpeg'), ('Image files', '*.png'), ('all files', '*.*')))
    newImage = Image.open(os.path.dirname(file) + '/'
                          + os.path.basename(file))
    newImage.save(os.path.dirname(file) + '/Compressed'
                  + os.path.basename(file), optimize=True,
                  quality=int(txt.get()))


lbl1 = Label(window, text='Quality percentage', font=('Arial Bold',
             20), padx=50, pady=30)
lbl1.grid(column=0, row=1)
txt = Entry(window, width=4)
txt.grid(column=1, row=1)
btn = Button(window, text='Select Image and Compress', command=clicked)
btn.grid(column=0, row=3)

window.mainloop()
