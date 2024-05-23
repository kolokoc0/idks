import tkinter as tk
import random
windows = tk.Tk()
width = 800
height =200
canvas = tk.Canvas(windows,width = width,height = height)
canvas.pack()
circle_size = 30
plates = {}
destroyable = {}
letters = 'ABCDEFGHIJ'
clicked_plates = {}
def create_plates():
    some_number = random.randrange(0,10)
    for i in range(10):
        x = i*(width//10)+circle_size+5
        y = height//2
        if i == some_number:
            destroyable[canvas.create_oval(x-circle_size,y-circle_size,x+circle_size,y+circle_size,fill="blue")] = letters[i]
        else:
            plates[canvas.create_oval(x-circle_size,y-circle_size,x+circle_size,y+circle_size,fill="blue")] = letters[i]
        canvas.create_oval(x-circle_size+5,y-circle_size+5,x+circle_size-5,y+circle_size-5)
        canvas.create_text(x,y,text=letters[i],fill="white", font="Arial 20")
    print(some_number)

def crack_plate(e):
    
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    a = clicked_plates.get(overlap[0],0)
    a+=1
    clicked_plates[overlap[0]] = a
    string = 'Viackrat si klikol na taniere: \n'

    if overlap[0] in destroyable:
        canvas.delete('all')
        for i in clicked_plates:
            if clicked_plates[i] >1:
                string += plates[i]
        canvas.create_text(150,100,text = string)










canvas.bind('<Button-1>',crack_plate)


create_plates()
windows.mainloop()