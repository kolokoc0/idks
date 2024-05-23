subor = open("objednane_jedla.txt","r",encoding = "utf-8")

dic = { }

orders = subor.readlines()
num = len(orders)

for line in orders:
    line = line.strip()
    num,code = line.split(" ")
    dic[code] = dic.get(code,0) + 1

vys = ''
temp = True
for i in dic:
    vys += i + ": " + str(dic[i]) + "\n"
    if dic[i]<20:
        print(f'Menej ako 20 ludi objednalo jedlo: {i}')
        temp = False
    elif dic[i]>=20 and temp!=False:
        temp = True
if temp == True:
    print("Kazde jedlo bolo objednane aspon 20x")
print(vys)
