import tkinter as tk
import random

win =tk.Tk()

canvas = tk.Canvas(width=700,height=500,bg='lightblue')
canvas.pack()

def draw_hill():
    hill=[]
    direction = random.choice((1,-1))
    print(direction)
    hill.append(0)
    hill.append(random.randint(250,500))
    peak = random.randint(200,600)
    print(peak)
    for increment in range(peak//10):
        new_y_val = hill[-1] + direction*random.randint(0,5)
        hill.append(increment*10+1)
        hill.append(new_y_val)

    direction = -1*direction

    for increment in range((700-peak)//10+10):
        new_y_val = hill[-1] + direction*random.randint(0,5)
        hill.append(increment*10+peak)
        hill.append(new_y_val) 
    
    hill = [0,500] + hill + [700,500]
    green = format(random.randint(50,255),'02x')
    color = '#00' + green + '00'

    canvas.create_polygon(hill,fill=color)

draw_hill()

def redraw(e):
    canvas.delete('all')
    for i in range(1):
        draw_hill()
canvas.focus_set()
canvas.bind('<space>',redraw)
win.mainloop()