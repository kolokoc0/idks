with open("D:\SKola\KuceraUlohy\Maturita_uloha_14\skok_do_dialky.txt","r",encoding="utf-8") as subor:
    jumps = subor.readlines()
countries = {}
longest_jumps = []
longest_jump = 0

for line in jumps:
    line = line.strip().split(" ")
    countries[line[1]] = countries.get(line[1],0) +1
    longest_jump = max([i for i in line if i.isnumeric()])
    longest_jumps.append((longest_jump,line[0]))
    longest_jump = 0

longest_jumps = sorted(longest_jumps)[::-1]
print('Zoznam krajin: \n' + ", ".join(countries))
print(f'Number of sportsmen: ')
for key in countries:
    print(f"{key} : {countries[key]}")
print(f"The longest jump was: {longest_jumps[0][0]}. Winners: ")
for winner in longest_jumps:
    if longest_jumps[0][0] == winner[0]:
        print(winner[1])
    else:
        pass






