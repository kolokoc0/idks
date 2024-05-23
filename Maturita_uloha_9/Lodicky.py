import tkinter, random

win = tkinter.Tk()

canvas = tkinter.Canvas(win,width=700, height=800)
canvas.pack()
numbers = {}
def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)


def creation():
    canvas.create_line(650,0,650,800,fill="red")
    for i in range(15):
        lodicka(30,30+i*50)
        numbers[i] = 30
def starter(e):
    movement()

def movement():
    overlap = canvas.find_overlapping(650,0,650,800)
    if len(overlap)==1:
        canvas.delete('all')
        canvas.create_line(650,0,650,800,fill="red")
        for i in range(15):
            num = random.randrange(1,11)
            a = numbers.get(i,30)
            a +=num
            numbers[i] = a
            lodicka(numbers[i],30+i*50)
        canvas.after(30,movement)
    elif len(overlap)>1:
        print(overlap[1],(overlap[1]-overlap[0])//2)
        canvas.create_text(200,400,text="Preteky vyhrala lodicka cislo: "+str((overlap[1]-overlap[0])//2),font=("Arial 20"))

        
creation()
canvas.bind("<Button-1>",starter)

win.mainloop()