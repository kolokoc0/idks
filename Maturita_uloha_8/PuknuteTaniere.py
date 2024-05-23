import tkinter as tk
import random

win = tk.Tk()

letters = ["A","B","C","D","E","F","G","H","I","J"]
circle_size = 30
circle_num = 10
width = 800
height = 100
circles = {}


canvas = tk.Canvas(win,width=width,height=height)
canvas.pack()

random = random.randrange(0,10)

for i in range(circle_num):
    x = i*(width//10)+35
    y = height//2
    if random == i:
        circles[(canvas.create_oval(x-circle_size,y-circle_size,x+circle_size,y+circle_size,fill="blue",tag="broken"))]=0
        canvas.create_oval(x-circle_size+10,y-circle_size+10,x+circle_size-10,y+circle_size-10,outline="black")
        canvas.create_text(x,y,text=letters[i],fill="white", font="Arial 20")
        print(i)
    else:
        circles[(canvas.create_oval(x-circle_size,y-circle_size,x+circle_size,y+circle_size,fill="blue"))]=0
        canvas.create_oval(x-circle_size+10,y-circle_size+10,x+circle_size-10,y+circle_size-10,outline="black")
        canvas.create_text(x,y,text=letters[i],fill="white", font="Arial 20")

def click(e):  
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)

    string = "Viackrat si klikol na taniere: "
    if overlap[0] in circles:
        a = circles.get(overlap[0],0)
        a +=1
        circles[overlap[0]] = a
        tag = canvas.itemcget(overlap[0],"tag")
        if tag =="broken" or tag=="broken current":
            canvas.delete("all")
            canvas.create_text(width//2,height//2-10,text="Gratulujem, oznacil si punknuty tanier !",font=("arial",20),fill="blue")
            for i in range(len(circles)):
                if circles[list(circles)[i]]>1:
                    string+= letters[i]
            canvas.create_text(width//2,height//2+30,text=string,font=("Arial",10),fill="red")

canvas.bind("<Button-1>",click)

win.mainloop()