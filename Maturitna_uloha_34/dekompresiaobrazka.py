with open('dekompresia_obrazka_1.txt','r') as file:
    first = file.readline()
    file = file.readlines()

product = 1
first = first.split(' ')
for i in first:
    product = product *int(i)
print(f'Obrazok ma pocet bodov: {product}')
def spracuj_obrazok(line):
    beg = False
    new_line = ''
    line = line.split(' ')
    if line[0] == '0':
        line.pop(0)
        beg = True
    for num in range(len(line)):
        if beg == True:
            new_line += int(line[num])*'1'
            beg = False
        else:
            new_line += int(line[num])*'0'
            beg = True
    return new_line





for line in file:
    line = line.replace('\n','')
    line = spracuj_obrazok(line)
    print(line)