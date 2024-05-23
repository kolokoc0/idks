from re import search
subor = open("hada.txt","r",encoding = "utf-8")
subor_new = open("hada_test.txt","w")

def hadatka(subor):
    games = subor.readlines()
    games = [game.strip() for game in games]
    vys = ""
    list = []
    co = 0

    longest = max([len(x) for x in games])

    num_games = len(games)
    for line in games:
        co = 0
        letter = line[0]
        for i in range(len(line)):
            if line[i]==letter:
                co +=1
            else:
                vys = letter + ' '+ str(co)
                co =1
                letter = line[i]
                list.append(vys)

        vys = letter + ' ' + str(co)
        list.append(vys)
        subor_new.write(" ".join(list) + '\n')
        list = [ ]
    print(list)

           

        
               
                
        

hadatka(subor)

