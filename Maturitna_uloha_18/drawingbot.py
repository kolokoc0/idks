import tkinter as tk


window = tk.Tk()

width = 1000
height = 1000

canvas = tk.Canvas(window,width = width,height=height,bg='white')
canvas.pack()

current = [width//2,height//2]
angle = 0

def actions():
    global current,angle
    command = widget.get()
    command = command.split(' ')
    print(command)

    if command[0] =='ciara':
        if angle%360==0:
            canvas.create_line(current[0],current[1],current[0],current[1]-int(command[1]))
            current[1] -= int(command[1])
        elif angle%360==90:
            canvas.create_line(current[0],current[1],current[0]+int(command[1]),current[1])
            current[0] += int(command[1])
        elif angle%360==180:
            canvas.create_line(current[0],current[1],current[0],current[1]+int(command[1]))
            current[1] += int(command[1])
        elif angle%360==270:
            canvas.create_line(current[0],current[1],current[0]-int(command[1]),current[1])
            current[0] -= int(command[1])
    elif command[0] == 'vpravo':
        angle +=90
    elif command[0] =='vlavo':
        angle-=90
        if angle == -90:
            angle = 270

    

widget = tk.Entry(window)
widget.pack()
button = tk.Button(window,text='Stlac', command = actions)
button.pack()

window.mainloop()