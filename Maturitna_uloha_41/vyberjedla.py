import tkinter as tk

file = open('vyber_jedla.txt','w')

width = 1000
height = 400

win = tk.Tk()

canvas = tk.Canvas(win,width = width,height=height)
canvas.pack()

canvas.create_text(500,50,font=('arial',40),text='VYBER JEDLA',fill='red')
colors = ['green','red','blue','orange']
for i in range(4):
    canvas.create_rectangle(width//4*i,100,width//4*(i+1),100+width//4,fill=colors[i])

te = tk.Label(win,width = 30, text='kod studenta')
te.pack()

entry = tk.Entry(win)
entry.pack()

def click(e):
    input = entry.get()
    if input.isnumeric() == True:
        overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
        color = canvas.itemcget(overlap[0],'fill')
        if color == 'blue':
            color = 'm'
        elif color == 'red':
            color = 'c'
        elif color == 'green':
            color = 'z'
        elif color == 'orange':
            color = 'o'
        file.write(f'{input} {color}' + '\n')


    


canvas.bind('<Button-1>',click)

win.mainloop()

file.close()