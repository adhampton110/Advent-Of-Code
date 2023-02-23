rucksacks = []
total = 0
with open("input.txt") as source:
    for line in source:
        line = line.strip("\n")
        rucksacks.append(line)

for item in rucksacks:
    half = int(len(item)/2)
    c1 = item[:half]
    c2 = item[half:]
    for i in range(len(c1)):
        if c1[i] in c2:
            if c1[i].isupper():
                ans = ord(c1[i].lower())-96+26
                total+=ans
            else:
                ans = ord(c1[i])-96
                total +=ans
            break
print(total)
group = 0 
for i in range(0,len(rucksacks),3):
    c1 = rucksacks[i]
    c2 = rucksacks[i+1]
    c3 = rucksacks[i+2]
    for i in range(len(c1)):
        if c1[i] in c2 and c1[i] in c3:
            if c1[i].isupper():
                ans = ord(c1[i].lower())-96+26
                group+=ans
            else:
                ans = ord(c1[i])-96
                group +=ans
            break
print(group)
