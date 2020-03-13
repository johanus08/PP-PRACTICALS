# Python program to draw on a canvas using tkinter
# Importing tkinter module
from tkinter import*

# Master window
root=Tk()

# Setting height width
canvas_width=500
canvas_height=500

# Canvas created
c=Canvas(root,width=canvas_width,height=canvas_height,bg="blue")
c.pack()

y=int(canvas_height/2)
c.create_line(10,y,canvas_width,y,fill="green")
coord=10,50,240,210
arc=c.create_arc(coord,start=90,extent=190,fill="red")
oval=c.create_oval(50,60,100,100)
