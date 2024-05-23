import tkinter as tk

expression = input('Daj vyraz ')
expression = expression.strip(' ')


window = tk.Tk()

width = 500
height = 200

canvas = tk.Canvas(window,width = width,height=height,bg='white')
canvas.pack()

colors = ['blue','green','red','yellow','brown','hotpink','cyan']

parentheses = []
num = 0

def check(expression):
    stack = []
    parenthes = []
    for i in range(len(expression)):
        if expression[i] in '()':
            parenthes.append(expression[i])

    for i in parenthes:
        if i == '(':
            stack.append(i)
        else:
            if len(stack)>0 and stack[len(stack)-1] == '(':
                stack.pop()
            else:
                return False
    if len(stack)>0:

        return False
    else:
        return True
    
y = 100


if check(expression):
    for i in range(len(expression)):
        x_start = 10
        gap = 5
        if expression[i] not in '()':
            canvas.create_text(x_start*i+30+gap*i,y,text=expression[i],fill='black',font=('Arial',20))
        else:
            if expression[i] == '(':
                num +=1
                canvas.create_text(x_start*i+30+gap*i,y,text=expression[i],fill=colors[num-1],font=('Arial',20))
            else:
                canvas.create_text(x_start*i+30+gap*i,y,text=expression[i],fill=colors[num-1],font=('Arial',20))
                num -=1
    canvas.create_text(100,y+50,text='Vyraz ma vyrovnane zatvorky',font=('Arial',10))
else:
    canvas.create_text(100,y+50,text='Vyraz nema vyrovnane zatvorky',font=('Arial',10))

window.mainloop()