import random

file = open('poprehadzovany_text_vstup2.txt',"r",encoding='utf-8')
file = file.readlines()
file_new = open('poprehadzovany_text2_vystyp.txt','w')
for line in file:
    line = line.strip()
    print(line)
print()
def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

def categories(word):
    toshuffle = ''
    notcharaf = ''
    notcharbe = ''
    i = 0
    while not word[i].isalpha():
        notcharbe += word[i]
        i+=1
    while i<len(word) and word[i].isalpha():
        toshuffle += word[i]
        i+=1
    notcharaf = word[i:]
    return (notcharbe,toshuffle,notcharaf)

for line in file:
    line = line.strip().split(" ")
    for i in range(len(line)):
        bef,shuff,aft = categories(line[i])
        if len(shuff) >2:
            shuff = shuff[0] + pomiesaj(shuff[1:-1:]) + shuff[-1]
        line[i] = bef + shuff + aft
    line = ' '.join(line) + "\n"
    file_new.write(line)
    print(line, end = "")
file_new.close()






 
        
            
        

