subor = open("meteo_stanice.txt",'r',encoding="utf-8")

def meto(subor):
    poc = 0
    temp = False
    vys = ""
    tep = 0
    priemer = 0
    for line in subor:
        poc +=1
        a = line[21:26:1]
        vys += a
        vys += '\n'
        a = a.replace(",",".")
        if '-' in a:
            a =  float(a[1::])*(-1)
        else:
            a = float(a[1::])
        if float(a)>float(tep):
            tep = float(a)
            naj = line[:3]
            tep = str(tep)
            if float(a)<0:
                tep = "-" + tep
            else:
                tep = "+" + tep
        priemer += float(a)
    priemer = priemer/poc
    print("pocet merani:",poc)
    print("najvacsia teplota:",tep, "Stanica:",naj)
    print("Merania:",'\n',vys)
    kon = (f'priemerna teplota vsetkych stanic: {priemer:.2f}')
    return(kon)
print(meto(subor))
            

