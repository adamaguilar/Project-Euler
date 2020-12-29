'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
'''
def value(name):
    value = 0
    for char in name:
        value = value + (ord(char) - 64)
    return value

file = open("Problem22.txt", "r")
names = sorted([name.strip('"') for name in file.readline().split(',')])
file.close()

total = 0

for name in range(0, len(names)):
    total = total + (value(names[name]) * (name + 1))

print(total)