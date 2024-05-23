import tkinter as tk

with open('noty.txt','r') as file:
    file = file.readlines()
file = ''.join(file)

width = 1000
height = 1000
dlzka = 400

windows = tk.Tk()

stupnica = 'cdefgah'

canvas = tk.Canvas(windows, height=height,width=width,bg='white')
canvas.pack()

def osnova(x,y,dlzka):
    for i in range(5):
        canvas.create_line(x,y+i*20,x+dlzka,y+i*20)


def draw_note(x,y):
    canvas.create_oval(x-7,y-6,x+7,y+6)

def do_everything(file):
    x = 20
    y = 10
    osnova(0,y,dlzka)
    pocet = 0
    for nota in file:
        draw_note(x,y+ 5 * 20 - (stupnica.find(nota)*10))
        x +=20
        pocet +=1
        if pocet+1 == dlzka//20:
            y += 140
            x = 20
            pocet = 0
            osnova(0,y,dlzka)

do_everything(file)

        














windows.mainloop()