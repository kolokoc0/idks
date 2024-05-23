subor = open('hada.txt','r',encoding="utf-8")
subor2 = open('hada_komp.txt','w')
def text (subor):
    prvy_riadok = 0
    poc = 0
    vys = ""
    poc2 = 1
    for line in subor:
        poc +=1
        if len(line)>prvy_riadok:
            prvy_riadok = len(line)
            if "\n" in line:
                prvy_riadok -= 1
        for i in range(1,len(line)):
            if line[i-1] != line[i]:
                subor2.write(line[i-1])
                subor2.write(str(poc2))
                poc2 = 1

            else:
                poc2 +=1
            if line[i] == '\n':
                subor2.write('\n')
    if subor.readline() == "":
        subor2.write(line[i-1])
        subor2.write(str(poc2))
    print('najdlhsia hra mala krokov:', (prvy_riadok))
    print("zapisane hry:", poc)
    
text(subor)
subor2 = open("hada_komp.txt","r")
subor2 = subor2.read()
print(subor2)
