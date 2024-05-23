with open('hlasovanie_1.txt','r') as file:
    file = file.readlines()


with open('hlasovanie_vypadnuti.txt','r') as fallout:
    fallout = fallout.readlines()

counting = 0
players = {}

for line in file:
    counting +=1
    line = line.strip('\n')
    players[line] = players.get(line,0)+1

no_fallout = []
with_fallout = []
print(f'Number of sent sms: {counting}')

for player in players:
    print(f'Sutaziaci: {player} dostal hlasov: {str(players[player])}')
    no_fallout.append((players[player],player))
    if player not in fallout:
        with_fallout.append((players[player],player))


print(f'Najmenej hlasov {min(no_fallout)[0]} celkovo ziskal: {min(no_fallout)[1]} ')
print(f'Najmenej hlasov {min(with_fallout)[0]} celkovo ziskal: {min(with_fallout)[1]}')






lowest_number = players[file[0].strip('\n')]

low_number = 10**6






