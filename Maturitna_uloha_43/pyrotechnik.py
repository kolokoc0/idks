import tkinter as tk
import random

width = 500
height = 500
num_cables = 5
colors = ['green','red','gray', 'blue','orange']

length = 300
size = 20

correct_cable = []

num = random.randint(0,num_cables-1)

win = tk.Tk()

canvas = tk.Canvas(win,width = width,height = height)
canvas.pack()

canvas.create_text(width//2,50,text='Pyrotechnik',font=('arial',30),fill='blue')
canvas.create_text(width//2,90,text='oznac spracny kablik',font=('arial',20))

time = '60'
clock = canvas.create_text(400,150+(size*num_cables)//2,text=time,font=('arial',30),fill='red')

temp = True

def clocking():
    global time
    canvas.update()
    time = str(int(time)-1)
    canvas.itemconfig(clock,text=time)
    if int(time)!=0 and temp == True:
        canvas.after(1000,clocking)
    elif int(time)<=0:
        canvas.delete('all')
        print('you lost')



def initiate():
    for i in range(num_cables):
        if i!=num:
            canvas.create_rectangle(50,150+i*size,50+length,150+(i+1)*size,fill=colors[i])
        elif i == num:
            correct_cable.append(canvas.create_rectangle(50,150+i*size,50+length,150+(i+1)*size,fill=colors[i]))
    clocking()

def click(e):
    global temp
    canvas.update()
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    print(num)
    print(overlap)
    if overlap[0] in correct_cable:
        temp = False
        canvas.create_text(width//2,300,text='Vyhral si',font=('arial',30))



initiate()

canvas.bind('<Button-1>',click)


win.mainloop()