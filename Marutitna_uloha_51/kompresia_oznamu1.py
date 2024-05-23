sent = input('Zadaj oznam: ')


sent = sent.split(' ')

print(f'Zoznam pozostava z {len(sent)} slov.')

new_sent = ''

for i in range(len(sent)):
    if i%2==0:
        new_sent += sent[i].upper()
    else:
        new_sent += sent[i].lower()
print(f'Stlaceny oznam: ',end='\n')
print(new_sent)

print(f'Naspat: ', end = '\n')
new_sent = ''
for i in sent:
    new_sent += i.upper() + ' '

print(new_sent[:-1:])
