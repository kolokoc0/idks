import tkinter as tk

with open('zastavky.txt','r') as file:
    file = file.readlines() 

width = 1000
height = 200


windows = tk.Tk()
i = 0
zastavky = [20*' '+line.strip() for line in file]

canvas = tk.Canvas(windows,width=width,height=height,bg='black')
canvas.pack()
print(zastavky)

def shower():
    global zastavka
    canvas.update()
    temp = zastavka[0:20:]
    canvas.itemconfig(textik,text=temp)
    zastavka = zastavka[1::]+zastavka[0]
    canvas.after(100,shower)


def change(e):
    global i,zastavka
    i+=1
    if i == len(zastavky)-1:
        zastavka = zastavky[i]+' POZOR!!! TREBA VYSTUPIT'
    elif i>=len(zastavky):
        i = 0
        zastavka = zastavky[i]
    else:
        zastavka = zastavky[i]
    print(zastavka)

textik=canvas.create_text(100,0,text='Davaj', font="Arial 50", fill="red", anchor="nw")
zastavka = zastavky[0]
shower()


windows.focus_set()
windows.bind('<Key>',change)

windows.mainloop()