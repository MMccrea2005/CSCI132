#part1

# f = open('roster.txt', 'w')
# f.close()

with open('roster.txt', 'w') as f:
    f.write('Alice\n')
    f.write('Bob\n')
    f.write('Fred\n')

    
names = ['Moe\n', 'Larry\n', 'Curly\n']
with open('roster.txt', 'a') as f:
    f.writelines(names)
    
# print('Done writing')

# reads
# with open('roster.txt.', 'r') as f:
#     contents = f.readlines()
    
# print(contents)
# print(type(contents))

#read one line at a time
# with open('roster.txt', 'r') as f:
#     for line in f:
#         print(line.strip())

with open('scores.txt', 'r') as f:
    allScores = f.readlines()
    intScores = []
    for s in allScores:
        intScores.append(int(s.strip()))
       
total = 0 
for item in intScores:
    total+=item

print(intScores)
print(total)
print(f'The average is {total / len(intScores)}')