with open('dopravny_prieskum.txt','r') as file:
    file = file.readlines()

travelling = 0
wagon = ''
not_stopping = []
for line in file:
    line = line.strip()
    ins , out, name = line.split(';',2)
    travelling = travelling + int(ins) - int(out)
    if 0<=travelling<=40:
        wagon = 'kratka'
    elif 40<travelling<=80:
        wagon = 'standard'
    else:
        wagon = 'dlha'

    if int(ins)<3 and int(out)<3:
        not_stopping.append(name)

    print(f'Zastavka: {name} cestujuci: {travelling}, odporucany typ elektricky: {wagon}, automat: {int(ins)>=10}')

print(f'Zastavky pri ktorych treba dat znamenie na stop: {" ,".join(not_stopping)}')