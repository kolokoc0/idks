import tkinter as tk

win = tk.Tk()

with open('ciernobiely_obrazok_1.txt','r') as file:
    size = file.readline()
    file = file.readlines()


size = size.split(' ')
size = (int(size[0]),int(size[1]))


canvas = tk.Canvas(height= 520,width = 600)
canvas.pack()


print(f'The dimensions are: {size[0]} and {size[1]}')
print(f'The number of points is: {size[0]*size[1]}')

shades = {i:0 for i in range(256)}

for line in file:
    for i in range(size[0]):
        shade = line[i*2:i*2+2:]
        shade = int(shade,16)
        shades[shade] = shades.get(shade,0)+1

max_shade = 0
for shade in shades:
    if shades[shade]>max_shade:
        max_shade = shades[shade]

print(f"Most frequented shade is shown: {max_shade}")

shades_values = [shades[i] for i in sorted(shades)]


print(shades_values)
print(len(shades_values))


mierka = (max_shade//500)+1


def graph(shades,mierka):
    for i in range(256):
        canvas.create_rectangle(i*2,500,i*2+2,500-shades[i]/mierka,width = 0,fill='gray')

graph(shades_values,mierka)



win.mainloop()