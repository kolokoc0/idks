with open('spokojnost_1.txt','r') as file:
    file = file.readlines()

counter = 0
good = {}
bad = {}



for line in file:
    counter +=1
    line = line.strip().split(' ')
    line = (line[0].split(':')[0],line[1])
    if line[1]=='áno':
        good[line[0]] = good.get(line[0],0)+1
    else:
        bad[line[0]] = bad.get(line[0],0)+1

good_sorted = sorted(good,key= lambda x: good[x],reverse= True)
bad_sorted = sorted(bad,key = lambda x: bad[x],reverse=True)
print(good_sorted)
print(bad_sorted)

print(f'Most satisfied customers during hour: {good_sorted[0]}, ood reviews: {good[good_sorted[0]]}')
print(f'Most dissatisfied customers during hour: {bad_sorted[0]} all bad reviews: {bad[bad_sorted[0]]}')

set_final = set(good_sorted)

for i in sorted(set_final):
    if i not in bad:
        print(f'V {i} hodine je spokojnych {good[i]/(good[i])*100:.2f}%')
    else:
        print(f'V {i} hodine je spokojnych {good[i]/(good[i]+bad[i])*100:.2f}%')







