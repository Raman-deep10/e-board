from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color
#from scipy.__config__ import show
from tkinter import filedialog
import os

root =Tk()
root.title("white board")
root.geometry("1800x900")
root.resizable(True,True)

current_x = 0
current_y = 0
color="black"

def locate_xy(work):
    global current_y , current_x
    current_x = work.x
    current_y = work.y

def addline(work):
    global current_x , current_y
    Canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=True)
    current_x = work.x
    current_y = work.y
def show_color(new_color):
    global color

    color=new_color

def new_canvas():
    Canvas.delete('all')
    color_palete()

#load images
logo = PhotoImage(file="Whiteboard-.png")
root.iconphoto(False,logo) 


color_panel =PhotoImage(file="color section.png")
Label(root,image=color_panel,bg="#f2f3f5").place(x=10,y=20)

ereaser = PhotoImage(file="eraser.png")
Button(root,image= ereaser,bg="#ffffff",command=new_canvas).place(x=30,y=410)

colors= Canvas(root,bg="#f2f3f5",width=37,height=320,border=10,bd=0)
colors.place(x=30,y=60)


#board
Canvas = Canvas(root,bg="white",width=930,height=500,cursor="hand2")
Canvas.place(x=100,y=10)

Canvas.bind('<Button-1>',locate_xy)
Canvas.bind('<B1-Motion>',addline)

#fill colour in panel

def color_palete():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill="gray")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('gray'))

    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('red'))

    id = colors.create_rectangle((10,100,30,120),fill="orange")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))

    id = colors.create_rectangle((10,130,30,150),fill="yellow")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('yellow'))

    id = colors.create_rectangle((10,160,30,180),fill="green")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('green'))

    id = colors.create_rectangle((10,190,30,210),fill="blue")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))

    id = colors.create_rectangle((10,220,30,240),fill="purple")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('purple'))

    id = colors.create_rectangle((10,250,30,270),fill="brown")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('brown'))

    id = colors.create_rectangle((10,280,30,300),fill="skyblue")
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('skyblue'))
color_palete()

################################   sider     ###################
current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root,from_=0,to=100,orient="horizontal",command=slider_changed,variable=current_value)
slider.place(x=30,y=530)
    
value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)

root.mainloop()
