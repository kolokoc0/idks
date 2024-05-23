import random

file = open('loteria_2.txt','r')
num_of_winners = {}
winning_nums = set()
while len(winning_nums)!=6:
    num = random.randrange(1,50)
    if num not in winning_nums:
        winning_nums.add(num)
for line in file:
    line = set(int(i) for i in line.strip().split(' '))
    print(winning_nums)
    print(line)
    both = winning_nums.intersection(line)
    print(both,len(both))
    if both and len(both)!=4:
        num_of_winners[len(both)] = num_of_winners.get(len(both),0)+1
print(sorted(num_of_winners.items(), key = lambda x:str(x[0])))
print(set(winning_nums))