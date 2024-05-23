import tkinter as tk

win = tk.Tk()

with open('komprimovany_obrazok_1.txt','r') as file:
    size = file.readline()
    file = file.readlines()



size = size.split(' ')
size = (int(size[0]),int(size[1]))

canvas = tk.Canvas(win,height=size[1],width = size[0],bg='white')
canvas.pack()





def draw(color):
    start_y = 0
    start_x = 0
    current_x = 0
    canvas.delete('all')
    for line in file:
        line = line.split(' ')
        for num in line:
            for i in range(int(num)):
                canvas.create_rectangle(current_x,start_y,current_x+1,start_y+1,fill=color,width = 0)
                current_x +=1
            if color=='white':
                color = 'black'
            else:
                color = 'white'
        current_x = start_x
        start_y +=1


draw('black')

def button_comm():
    draw('white')

button = tk.Button(text='negativ',command=button_comm)
button.pack()


win.mainloop()