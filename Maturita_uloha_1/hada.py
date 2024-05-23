import tkinter as tk


windows = tk.Tk()
width = 500
height = 500
canvas = tk.Canvas(windows, width= width, height=height,background='white')
canvas.pack()

vector = (0,-1)

def movement():
    canvas.move(snek[0],vector[0],vector[1])
    hlava_coords = canvas.coords(snek[0])
    overlap = canvas.find_overlapping(hlava_coords[0],hlava_coords[1],hlava_coords[2],hlava_coords[3])
    if len(overlap)>3:
        canvas.delete('all')
        print('you lost')
    else:
        snek.append(canvas.create_rectangle(hlava_coords[0],hlava_coords[1],hlava_coords[2],hlava_coords[3], fill='black'))
        canvas.after(100,movement)


def prepare():
    global snek
    hlava = canvas.create_rectangle(width/2,height/2,width/2+1, height/2+1,fill='black')
    snek = [hlava]
    movement()
def change_vector(e):
    global vector
    if e.keysym == "Right":
        vector = (1,0)
    elif e.keysym == 'Left':
        vector = (-1,0)
    elif e.keysym == 'Up':
        vector = (0,-1)
    elif e.keysym == 'Down':
        vector = (0,1)
canvas.focus_set()
windows.bind('<Key>',change_vector)

prepare()











windows.mainloop()