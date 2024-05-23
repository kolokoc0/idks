import tkinter as tk
import random

with open('krizovka1-2.txt','r') as file:
    file = file.readlines()

file = [line.strip().split(' ') for line in file]
naj = 0
for line in file:
    temp = int(line[0])
    if temp>naj:
        naj = temp





windows = tk.Tk()
width = 1000
height = 1000

canvas = tk.Canvas(windows,width=width,height=height)
canvas.pack()
cell_size = 30
x = 10
y = 10
def create_line(line,x,y,vyplnit,grey_cell):
    print(line)
    for i in range(len(line[1])):
        if not vyplnit:
            if grey_cell ==i:
                canvas.create_rectangle(x+cell_size*i,y,x+cell_size*(i+1),y+cell_size,fill='grey')
            else:
                canvas.create_rectangle(x+cell_size*i,y,x+cell_size*(i+1),y+cell_size)
        else:
            if grey_cell ==i:
                canvas.create_rectangle(x+cell_size*i,y,x+cell_size*(i+1),y+cell_size,fill='grey')
            else:
                canvas.create_rectangle(x+cell_size*i,y,x+cell_size*(i+1),y+cell_size)
            canvas.create_text(x+cell_size*i+15,y+cell_size/2,text=line[1][i])
def create_whole(vstup_x,y,vyplnit):
    for line in file:
        x = vstup_x
        x = x + (naj)*cell_size - int(line[0])*cell_size
        gray_cell = int(line[0])-1
        create_line(line,x,y,vyplnit,gray_cell)
        y += cell_size

create_whole(10,10,False)
create_whole(500,10,True)

windows.mainloop()