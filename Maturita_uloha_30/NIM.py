import tkinter as tk 
import random

win = tk.Tk()

canvas = tk.Canvas(width=650, height=200)
canvas.pack()



def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')

def draw_matches(player,matches_num):
    x = 20
    y = 90
    canvas.delete('all')
    for i in range(matches_num):
        zapalka(20+ x*i,y)
        create_text(player,matches_num)

def create_text(player,matches_num):
    canvas.create_text(100,20,text = 'Turn of player: ' + player)
    canvas.create_text(100,30,text='Num of matches left: '+ str(matches_num))

def end(player):
    canvas.delete('all')
    canvas.create_text(100,150,text='Game was won by player: ' + player)

def typing(e):
    global matches_num,player
    if 1 <= int(e.char)<=3:
        if matches_num - int(e.char) >0:
            matches_num -= int(e.char)
            if player=='1':
                player = '2'
            else:
                player = '1'
            draw_matches(player,matches_num)
        else:
            end(player)
        
        
        




player = '1'
matches_num = 15

draw_matches(player,matches_num)

canvas.focus_set()
canvas.bind('<Key>',typing)
win.mainloop()