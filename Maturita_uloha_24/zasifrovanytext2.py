import random
file1 = open('vstupny_text.txt','r+')
file2 = open('vystupny_text.txt','r+')
sifring = input('Ak chces sifrovat napisa Ano: ')
if sifring == 'Ano':
    sifring = 1
else:
    sifring = -1
    file1,file2 = file2,file1

def deorcypher(input,sifring):    
    line = list(input.strip('\n'))
    if sifring ==1:
        key = random.randrange(1,25)
    else:
        key = ord(line[0])-96
        a = line.pop(0)
    for letter in range(len(line)):
        if 'a'<=line[letter]<='z':
            line[letter] = chr((((ord(line[letter])-97)+(sifring)*((key)))%26)+97)
    if sifring ==1:
        line = chr(key+96)+ (''.join(line))
    else:
        line = (''.join(line))
    return (line)
    

for line in file1:
    print(line)
    line = line.strip('\n')
    if line!='':
        line = deorcypher(line,sifring)
        print(line)
        line += '\n'
        file2.write(line)
    if line =='':
        file2.write('\n')
file2.close()
    
