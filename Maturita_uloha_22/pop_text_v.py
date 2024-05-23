import random
import time
start = time.time()

for i in range(1000):

    def pomiesaj(retazec):
        pismenka = list(retazec)
        random.shuffle(pismenka)
        return ''.join(pismenka)

    def ocisti_slovo(slovo):
        ciste_slovo = ''
        zly_zaciatok = ''
        zly_koniec = ''
        i = 0
        while slovo[i] in vynechat:
            zly_zaciatok += slovo[i]
            i += 1
        while i < len(slovo) and not (slovo[i] in vynechat): # {riadok A}
            ciste_slovo += slovo[i]
            i += 1
        zly_koniec = slovo[i:]
        return zly_zaciatok, ciste_slovo, zly_koniec

    vynechat = '.,!?():#@~[]0123456789<>{}^%*-+/\\'
    subor1 = open('poprehadzovany_text_vstup2.txt', 'r')


    for riadok in subor1:
        print(riadok, end='')
        slova = riadok.strip().split()
        for i in range(len(slova)):
            pred, stred, koniec = ocisti_slovo(slova[i])
            if len(stred) > 2: # {riadok B}
                stred = stred[0] + pomiesaj(stred[1:-1]) + stred[-1]
            slova[i] = pred + stred + koniec
        riadok = ' '.join(slova) + '\n'
        print(riadok, end='')

    subor1.close()

end = time.time()

print((end-start)*10**3, 'ms')