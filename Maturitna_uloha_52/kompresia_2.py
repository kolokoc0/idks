sent = input('Zadaj vetu: ')
sent = sent.split(' ')

new_sent =''

for i in sent:
    new_sent += i.capitalize()

print(f'Stlaceny tvar: ')

print(new_sent)

new_sent = ''

for i in sent:
    new_sent += i.upper() +' '

print('Konecny tvar: ')

print(new_sent)