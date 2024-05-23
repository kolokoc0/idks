with open('hlasovanie_1.txt','r') as file:
    file = file.readlines()
files = []
for i in range(int(sorted(set(file))[0])-int(sorted(set(file))[0]),int(sorted(set(file))[-1])-int(sorted(set(file))[0])):
    line = str(int(sorted(set(file))[0])+i)
    line = line.strip('\n')
    f = open(str(line),'w')
    files.append(f)

for index,item in enumerate(file):
    item = int(item.strip('\n'))
    try:
        files[item-5220].write(str(index+1))
        files[item-5220].write('\n')
    except:
        print(item,index)

for f in files:
    f.close()
    
