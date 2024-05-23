with open('kompresia_obrazka_1.txt','r') as file:
    first = file.readline()
    file = file.readlines()
first = first.split(' ')
prod = 1
for i in first:
    prod = prod*int(i)
print(f'Pocet vsetkych bodov je: {prod}')

new_filetext = ''
def spracuj_riadok(line):
    count = 1
    new_line = ''
    if line[0] =='1':
        new_line += '0' + ' '
    line = line.replace('\n','')
    for num in range(1,len(line)):
        if line[num]==line[num-1]:
            count +=1
        else:
            new_line += str(count) + ' '
            count = 1
    new_line += str(count)

    return new_line
        


new_file = open('compressed1.txt','w')
new_file.write(' '.join(first))
for line in file:
    line = spracuj_riadok(line)
    line += '\n'
    new_file.write(line)
new_file.close()

        
        
        
        
    



