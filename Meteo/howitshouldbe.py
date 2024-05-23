subor = open('meteo_stanice.txt', 'r')
pocet = 0
zoz = []
teploty = []
ibateploty = []
for r in subor:
    info = r.strip()
    teplota = info[21:26]
    teplota = float(teplota.replace(',', '.')) # {riadok A}
    teploty.append((teplota, info[:3])) # {riadok B}
    ibateploty.append(teplota)
    print(teplota)
    pocet += 1
    zoz.append(info)

subor.close()
print('Počet meraní:', pocet)
print('Maximum bolo v stanici:', max(teploty)[1],max(teploty)[0])
priemer = sum(ibateploty)/len(teploty)
print('Priemerná teplota bola: {:5.2f} stupňov'.format(priemer))