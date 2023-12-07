import re

with open("Project Euler/input.txt") as f:
    data = f.read()

names = re.findall(r'[A-Z]+', data)
names.sort()

tot = 0
for i in range(len(names)):
    tot += (i+1) * sum([ord(c) - 64 for c in names[i]])

print(tot)