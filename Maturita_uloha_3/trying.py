import tkinter as tk
win=tk.Tk()
fr=open("zastavky.txt","r",encoding="UTF-8")
sirka_display=20
zt=""

zobraz_text=" "*20+"Fero"
def zobrazovacka():
    global zobraz_text
    canvas.update()
    temp=zobraz_text[0:20:]
    zt=temp
    canvas.itemconfig(textik,text=temp)
    zobraz_text=zobraz_text[1::]+zobraz_text[0]
    canvas.after(100,zobrazovacka)

canvas=tk.Canvas(width=500, height=100, bg="black")
canvas.pack()
textik=canvas.create_text(0,0,text=zt, font="Arial 25", fill="red", anchor="nw")
#for i in fr:
    #print(i)
zobrazovacka()

win.mainloop()