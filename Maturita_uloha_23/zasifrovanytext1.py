#in_text = open('vstupny_text.txt','r')
#in_text = in_text.readlines()
zas_text = open('zasifrovany_text_1.txt')
in_text = zas_text.readlines()

num_key = 0

key = input('Kluc, len male znamienka: ')
sifring = input('Ches sifrovat, ak hej napis Ano: ')

if sifring == 'Ano':
    sifring = 1
else:
    sifring = -1

def deorcypher(input,key,sifring):   
    line = list(input.strip('\n'))
    num_key = 0
    for letter in range(len(line)):
        if 'a'<=line[letter]<='z':
            line[letter] = chr((((ord(line[letter])-97)+(sifring)*((ord(key[num_key])-96)))%26)+97)
        num_key = (num_key +1)%len(key)
    return (''.join(line))
    
file1 = open('zasifrovany_text_1.txt','r')
file2 = open('vystup.txt','w')

for line in file1:
    print(line)
    line = deorcypher(line,key,sifring)
    line += '\n'
    print(line)
    file2.write(line)


file2.close()

line = input("Zadaj co chces za/desifrovat: ")
print(line)
line = deorcypher(line,key,sifring)
print(line)
