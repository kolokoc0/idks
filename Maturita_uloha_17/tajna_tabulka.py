sentence = input("Zadajte vstup: ").upper()
table = {' ':0,'A':1,'B':11,'C':111,'D':2,'E':22,'F':222,'G':3,'H':33,'I':333,'J':4,'K':44,'L':444,'M':5,'N':55,'O':555,
         'P':6,'Q':66,'R':666,'S':7,'T':77,'U':777,'V':8,'W':88,'X':888,'Y':9,'Z':99}
table_lst = list(table)[1::]
count = [0]*10
print(list(table))
for letter in sentence:
    print(f'{str(table[letter])}', end = ' ')
    if letter == ' ':
        count[0] +=1
    else:
        place = (table_lst.index(letter))//3+1
        number = (len(str(table[letter])))
        count[place] +=number
print(count)
print()

print("The most pushed buttons were on positions: ", end = ' ')
print(f'{count.index(max(count))}', end = ' ')



