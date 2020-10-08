import sys


sum = 0

with open("a.txt", 'r') as f:
    contents = f.read()
number_list = contents.split()
# number_list.remove('')

for i in range(0, len(number_list)): 
    number_list[i] = int(number_list[i])
    sum = sum + number_list[i]

print(number_list)
print(sum)