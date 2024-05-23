with open('ucenie_sa_slovicok.txt','r') as file:
    file = file.readlines()


choice = input('ak mam zadavat anglicke napic A inak hocico: ')

counter = 0
sk = file[::2]
en = file[1::2]

a,b = sk,en

if choice=='A':
    a,b = b,a

while len(a)>0:
    word1 = a.pop(0).strip()
    word2 = b.pop(0).strip()
    answer = input(f'Preklad slova {word1} je: ')
    if answer!=word2:
        counter+=1
        a.append(word1)
        b.append(word2)
        print(f'Nespravne!')
    else:
        print(f'Spravne')
print(f'Konecne done, pocet zlych odpovedi: {counter}')

