import random


with open('obesenec.txt','r') as file:
    file = file.readlines()

word = list(random.choice(file).strip())

print(word)

counter = 0
word_dots = ['.']*len(word)



while counter!=10 and word_dots!=word:
    print(''.join(word_dots))
    guess = input('Guess a letter: ')
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                word_dots[i] = guess
    else:
        counter +=1

if word_dots == word:
    print('COngrats')
else:
    print('You lost')





