import random

questions = [(random.randint(1,10),random.randint(1,10)) for i in range(10)]
points = 0
count = 0

while len(questions)!=0:
    question = questions.pop(0)
    answer = str(question[0] * question[1])
    inp = input(f'{question[0]} x {question[1]} = ')
    if inp==answer:
        if count!=10:
            points +=1
            count+=1
    else:
        questions.append(question)

print(points)
