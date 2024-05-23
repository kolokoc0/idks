subor = open("sutaz_vbehu.txt","r",encoding="utf-8")

games = subor.readlines()
num_games = len(games)
secs = []
names = []
for line in games:
    name,sec = line.strip().split(" ")
    names.append(name)
    secs.append(sec)

print(f"Pocet sutaziacich sportovcov: {num_games}")
for i in range(num_games):
    print(f'Sutaziaci {names[i]} dobehol do ciela za {secs[i]} sekund.')

best_time = min(secs)
best_name = names[secs.index(best_time)]
best_time = str(int(best_time)//60) + " min. "+ str(int(best_time)%60) + " sek."

print(f"Najlepsi sutaziaci bol {best_name} s casom {best_time}")