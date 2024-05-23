
subor = open("bus_vytazenost.txt","r")

buses = subor.readlines()
num_buses = len(buses)-1
over_names = []
over_num = []
names = []
limit = int(buses[0].strip())
current_num = 0

for line in buses[1::]:
    line= line.strip()
    print(line)
    inside, outside, name = line.split(' ',2)
    names.append(name)
    current_num = current_num + int(inside) - int(outside)
    if current_num>limit:
        over_names.append(name)
        over_num.append(current_num)

print(f'Zastavok je: {num_buses}')
print('Zastavky: ' + ", ".join(names))
print(f'Po nastupeni limit bol prekroceny na zastavkach: {", ".join(over_names)}')
print(f'Najviac ludi nad ramec kapacity bolo: {max(over_num)} na zastavke: {over_names[over_num.index(max(over_num))]}')

