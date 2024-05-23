text = open("objednane_jedla.txt","r",encoding = "utf-8" )
dict = {}
pocet = 0
for line in text:
    jedlo = line.split(" ")
    jedlo = jedlo[1].strip("\n")
    pocet +=1
    dict[jedlo] = dict.get(jedlo,0) +1
print("Celkovy pocet objednavok: " + str(pocet))
a = ""
for jedlo in dict:
    print("Kod: " + jedlo + " pocet objednavok: " + str(dict[jedlo]))
    if dict[jedlo]<20:
        a = a + jedlo + ", "
a = a[:-2:]
if a != "":
    print("Jedla: " + a + " si objednalo menej ako 20 ludi")
else:
    print("Vsetky jedla objednane")

