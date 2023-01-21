

from tkinter import *
import tkinter as tk
from tkinter import filedialog as tkFileDialog

from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("650x550")

canvas= Canvas(root, width= 500, height= 500)
canvas.pack(side = tk.LEFT)
def image():
    global filename
    filename = tkFileDialog.askopenfilename()
    Imag = Image.open(filename)
    if Imag.width >= 500 and Imag.width <= 999:
        basewidth = Imag.width / 1.5
    elif Imag.width >= 1000 and Imag.width <= 1999:
        basewidth = Imag.width / 2
    elif Imag.width >= 2000:
        basewidth = Imag.width / 4
    else:
        basewidth = Imag.width
    
    wpercent = (basewidth/float(Imag.size[0]))
    hsize = int((float(Imag.size[1])*float(wpercent)))
    Imag = Imag.resize((int(basewidth),hsize), Image.Resampling.BILINEAR)
    DisplayImage = ImageTk.PhotoImage(Imag)
    canvas.create_image(10,10,anchor = NW,image=DisplayImage)
    root.DisplayImage = DisplayImage
    canvas.pack(side = tk.LEFT)


def bubble():
    try:
        global filename
        bubble = tkFileDialog.askopenfilename()
        img = Image.open(filename)
        basewidth = img.width
        baseheight = img.height / 2
        bubbleimg = Image.open(bubble)
        bubbleimg = bubbleimg.resize((int(basewidth), int(baseheight)))
        img.paste(bubbleimg, (0, 0), mask=bubbleimg)
        img.save('bubbled.gif')
        if img.width >= 500 and img.width <= 999:
            basewidth = img.width / 1.5
        elif img.width >= 1000 and img.width <= 1999:
            basewidth = img.width / 2
        elif img.width >= 2000:
            basewidth = img.width / 4
        else:
            basewidth = img.width
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((int(basewidth), hsize), Image.Resampling.BILINEAR)
        DisplayImage = ImageTk.PhotoImage(img)
        canvas.create_image(10, 10, anchor=NW, image=DisplayImage)
        root.DisplayImage = DisplayImage
        canvas.pack(side = tk.LEFT)
        ErrorOutput.config(text = "Success!")
    except:
        ErrorOutput.config(text = "Error occured! Do you have an image? Images must be either .png or .jpeg")





ImageSelect = Button(
    root,
    text='Add Image', 
    command=image,
    width = 15,
    height = 2
).pack(anchor = SE, expand = tk.FALSE, padx=10, pady=10)

BubbleSelect = Button(
    root, 
    text='Add Speechbubble', 
    command=bubble,
    width = 15,
    height = 2
).pack(anchor = SE, expand = tk.FALSE, padx=10, pady=10)

ErrorOutput = Message(
    root, 
    text='',
    width = 115
)
ErrorOutput.pack(side = RIGHT, expand = tk.FALSE, padx=10, pady=10)

root.mainloop()
