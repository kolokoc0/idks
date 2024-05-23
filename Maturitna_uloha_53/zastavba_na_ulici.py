import tkinter as tk

with open('zastavba_na_ulici.txt','r') as file:
    buildings_file = file.readlines()


win = tk.Tk()

height = 200
width = 1000

buildings = []
highlighted_lines = []
canvas = tk.Canvas(win,width=width,height=height)
canvas.pack()




def draw_base():
    x_current = 0
    for line in buildings_file:
        line = line.strip().split(' ')
        line = (int(line[0]),int(line[1]))
        buildings.append([x_current,x_current+line[0],line[1]])
        if line[1]!=0:
            canvas.create_rectangle(x_current,height,x_current+line[0],height-line[1],fill='gray')
        else:
            canvas.create_line(x_current,height,x_current+line[0],height,fill='green',width=5)
        x_current += line[0]

draw_base()

def highlight(highlighted_lines):
    diff = int(entry.get())
    for i in range(1,len(buildings)):
        heights = (buildings[i-1][2],buildings[i][2])
        if abs(heights[0]-heights[1])>=diff:
            if 0 not in heights:
                highlighted_lines.append(canvas.create_line(buildings[i][0],height-min(heights),buildings[i][0],height-max(heights),fill='red',width = 5))
    return highlighted_lines

def starter():
    global highlighted_lines
    for line_id in highlighted_lines:
        canvas.delete(line_id)
    highlighted_lines.clear()
    highlight(highlighted_lines)



entry = tk.Entry(win,text='diff')
entry.pack()

button = tk.Button(win,text='click me',command=starter)
button.pack()



win.mainloop()