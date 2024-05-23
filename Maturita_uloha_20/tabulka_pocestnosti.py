with open('tabulka_pocetnosti.txt','r') as file:
    file = file.readlines()

letters = {chr(65+i) : 0 for i in range(26)}

for line in file:
    print(line, end = " ")
    line = line.strip()
    for char in line:
        if char.isalpha():
            letters[char.upper()] = letters.get(char.upper(),0) +1
letters = {key:value for key,value in sorted(letters.items())}

print()

for key in letters:
    if letters[key]!=0:
        print(f'{key} : {letters[key]}', end = "\n")

print(f'Missing letters: ')

for i in letters:
    if letters[i] == 0:
        print (i, end = ", ")