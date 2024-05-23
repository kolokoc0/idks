with open('spokojnost_1.txt') as file:
    file = file.readlines()

counter = 0
counter_days = 1
reactions_hours = {}
reactions_days = {}
hours = []


for line in file:
    counter +=1
    line = line.strip().split(' ')
    line = (line[0].split(':'))
    reactions_hours[line[0]] = reactions_hours.get(line[0],0)+1
    hours.append(float(line[0]+'.'+line[1]))


print(f'Celkovy pocet zaznamenanych reakcii: {counter}')

for i in sorted(reactions_hours):
    print(f'V {i}. hodine bolo: {reactions_hours[i]} reakcii.')

for i in range(1,len(hours)-1):
    time_prev = hours[i-1]
    time_cur = hours[i]
    if time_prev>time_cur:
        reactions_days[counter_days] = reactions_days.get(counter_days,0)+1
        counter_days +=1
    else:
        reactions_days[counter_days] = reactions_days.get(counter_days,0)+1
print(f'Pocet dni: {len(reactions_days)}')


for i in reactions_days:
    print(f'V {i}. den bolo: {reactions_days[i]} reakcii.')



