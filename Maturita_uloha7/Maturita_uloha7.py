import random


num_students = int(input("Pocet studentov: "))
num_questions = int(input("Pocet otazok: "))
students = []
questions = []
while num_students>num_questions:
    num_questions = int(input(f"Pocet otazok je mensi ako {num_students}  studentov. Prosim zadajte nove cislo otazok: "))

for i in range(num_students):
    students.append(i+1)
for i in range(num_questions):
    questions.append(i+1)

random.shuffle(students)
#ordermatters="Yes"
try:
    if ordermatters:
        odd_questions = questions[::2]
        even_questions = questions[1::2]
        random.shuffle(odd_questions)
        random.shuffle(even_questions)
        questions = [ ]
        for i in range(len(odd_questions)):
            try:
                questions.append(even_questions[i])
                questions.append(odd_questions[i])
            except:
                questions.insert(0,odd_questions[-1])
except:
    random.shuffle(questions)

print(f'Poradie, studenti a cisla otazok: ')

for i in range(len(students)):
    print(f'{i+1}. student: {students[i]}, otazka: {questions[i]}')





