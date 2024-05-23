import random
with open('virus.txt','r') as file:
    file = file.readlines()

file2 = open('vystup_virust.txt','w')
print(''.join(file))
new_file = []
if random.randrange(1,3) ==2:
    while len(file)!=0:
        ran_line = file.pop(file.index(random.choice(file)))
        new_file.append(ran_line)
    file = new_file
for line in file:
    new_line = []
    line = line.strip('\n').split(" ")
    if random.randrange(1,3)==2:
        while len(line)!=0:
            ran_word = line.pop(line.index(random.choice(line)))
            new_line.append(ran_word)
        line = new_line
    for word in range(len(line)):
        if random.randrange(1,3) ==2:
            line[word] = line[word][::-1]
    file2.write(' '.join(line))
    file2.write('\n')

file2.close()




