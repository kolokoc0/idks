import tkinter as tk
import random
width = 500
height = 500
size = 10
size_eater = 20
num_of_apples = 20
window = tk.Tk()

canvas = tk.Canvas(window,width=width,height=height,bg='white')
canvas.pack()
apples = []

for i in range(num_of_apples):
    x = random.randrange(size,width-size)
    y = random.randrange(size,height-size)
    apples.append(canvas.create_oval(x-size,y-size,x+size,y+size,fill='red'))

eater = canvas.create_oval(20,20,size_eater+20,size_eater+20,fill='blue')

vector = (2,0)

def change_vector(e):
    global vector
    if e.char == 'w':
        vector = (0,-2)
    elif e.char =='s':
        vector = (0,2)
    elif e.char == 'd':
        vector = (2,0)
    elif e.char == 'a':
        vector = (-2,0)

def movement():
    global vector
    coordinates = canvas.coords(eater)
    x1 = coordinates[0]
    y1 = coordinates[1]
    x2 = coordinates[2]
    y2 = coordinates[3]
    if vector!=(0,0):
        if x2>=width-size:
            vector = (-2,0)
        elif y1<=0+size:
            vector = (0,2)
        elif y2>=height-size:
            vector = (0,-2)
        elif x1<=0+size:
            vector = (2,0)

    overlap = canvas.find_overlapping(x1,y1,x2,y2)
    print(overlap)
    if len(overlap)>=2:
        destroy_overlap(overlap[:-1:])
        

    if len(apples)>0:
        canvas.move(eater,vector[0],vector[1])
        canvas.after(10,movement)
    else:
        canvas.delete('all')
        canvas.create_text(100,100,text='You Won!', font=('Arial',16))
    

movement()

def destroy_overlap(overlap):
    for i in overlap:
        canvas.delete(i)
        apples.pop(apples.index(i))







window.bind('<KeyPress>',change_vector)



window.mainloop()