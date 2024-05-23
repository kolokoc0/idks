file = open(f'mena_zamestnancov.txt')
new_file = open(f"vystup.txt","w")
file = file.readlines()
firstnames = []
surnames = []
print(file)
for i in range(len(file)//2):
    line = file[i].strip()
    firstnames.append(line)
    surnames.append(file[i+4].strip())

longest_firstnames = sorted(firstnames, key=len, reverse=True)
longest_surnames = sorted(surnames,key = len, reverse=True)
print(longest_firstnames,longest_surnames)
print(f'Pocet mien: {len(file)//2}')
print(f'Najdlhsie krstne meno ma dlzku: {len(longest_firstnames[0])}')
print(f'Najdlhsie priezvisko ma dlzku: {len(longest_surnames[0])}')

for i in range(len(firstnames)):
    new_file.write(f"{firstnames[i]:<15s} {surnames[i]}" + "\n")


new_file.close()
