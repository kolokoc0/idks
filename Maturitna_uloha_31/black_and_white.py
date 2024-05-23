import tkinter as tk

def draw_rectangle(x,y,colour):
    canvas.create_rectangle(x,y,x+1,y+1,width= 0,fill=colour)

def draw(all_colour):
    canvas.delete('all')
    file = open('ciernobiely_obrazok_1.txt','r')
    line = file.readline()
    y = 0
    for line in file:
        line = line.strip()
        x = 0
        for letter in range(width):
            shade = line[letter*2:letter*2+2:]
            if not all_colour:
                colour = 'black'
                if shade>'7f':
                    colour = 'white'
            else:
                colour =  '#' + 3*shade
            draw_rectangle(letter,y,colour)
        canvas.update()
        y+=1
    file.close()

def Black_white():
    draw(all_colour=False)



file = open('ciernobiely_obrazok_1.txt','r')
dimensions = file.readline().split(' ')
width = int(dimensions[0])
height = int(dimensions[1])
file.close()
win = tk.Tk()
canvas = tk.Canvas(width=width,height=height)
canvas.pack()

button= tk.Button(text='only black and white',command=Black_white)
button.pack()

draw(True)
win.mainloop()