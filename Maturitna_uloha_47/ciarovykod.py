import tkinter as tk

with open('ciarovy_kod_3.txt','r') as file:
    file = file.readlines()

height =300
width = 400
gap = 40

line_length = 80
line_width = 0
lim = 0


win = tk.Tk()

canvas = tk.Canvas(win,width = width,height=height)
canvas.pack()






def draw(lim):
    canvas.delete('all')
    canvas.update()
    num = len(file)-lim
    if num>4:
        num = 4
    x_start = 20
    x_current = x_start
    y_start = 10
    for i in range(num):
        if i ==2:
            y_start =10
            x_start = x_current+gap
            x_current = x_start
        x_current = x_start
        line = file[i+lim].strip('\n')
        for j in  range(len(line)):
            size = line[j]
            if size !='0':
                if j==0 or j==len(line)-1:
                    canvas.create_rectangle(x_current,y_start,x_current+int(size),y_start+80,fill='black',width = 0)
                else:
                    canvas.create_rectangle(x_current,y_start,x_current+int(size),y_start+60,fill='black',width = 0)
                canvas.update()
            x_current = x_current+10
        canvas.create_text(60*(i//2+1)+(gap+20)*(i//2),y_start+70,font=('arial',10),text=line)
        canvas.update()
        y_start +=130
        


draw(lim)



def change_lim(e):
    global lim
    print(e.char)
    if lim<len(file):
        lim +=4
    else:
        lim += len(file)-lim
    draw(lim)


canvas.focus_set()
canvas.bind('<Key>',change_lim)
win.mainloop()