with open('ciernobiely_obrazok_1.txt','r') as file:
    first = file.readline()
    file = file.readlines()

first = first.split(' ')
product = 1
for i in first:
    product = product *int(i)
print(f'Pocet blokov v subore je: {product}')


def spracuj_riadok(line):
    pairs = [line[i:i+2] for i in range(0,len(line),2)]
    new_line = ' '.join(['1' if val >'7F' else '0' for val in pairs])
    return new_line





for line in file:
    line = line.replace('\n','')
    line = spracuj_riadok(line)
    print(line)
