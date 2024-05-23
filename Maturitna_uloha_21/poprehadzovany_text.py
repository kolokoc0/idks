from random import shuffle
with open('poprehadzovany_text1_vstup.txt',"r",encoding='windows-1250') as file:
    file = file.readlines()

new_file = open('poprehadzovany_text_vystup.txt','w', encoding = 'windows-1250')

riadok = ""
for line in file:
    line = line.strip().split(" ")
    for word in line:
        word = list(word)
        toshuffle = word[1:len(word)-1:]
        shuffle(toshuffle)
        word = word[0] + ''.join(toshuffle) + word[-1]
        riadok += word + " "
    print(riadok[:-1:])
    new_file.write(riadok[:-1:]+"\n")
    riadok = ""
        


