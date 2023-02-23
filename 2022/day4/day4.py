pairs = []
with open("input.txt") as source:
    for line in source:
        line = line.strip("\n")
        line = line.split(",")
        p1 = line[0].split("-")
        p2 = line[1].split("-")
        pairs.append([p1,p2])
total = 0
for pair in pairs:
    p1 = pair[0]
    p2 = pair[1]
    #p1 entrapped in p2
    if (int(p2[0]) <= int(p1[0])) and (int(p1[1]) <= int(p2[1])):
        total += 1
    #p2 entrapped in p1
    elif (int(p1[0]) <= int(p2[0])) and (int(p2[1]) <= int(p1[1])):
        total += 1
    else:
        pass
print(total)

newTotal = 0
for pair in pairs:
    p1 = pair[0]
    p2 = pair[1]
    p1 = [x for x in range(int(p1[0]),int(p1[1])+1)]
    p2 = [x for x in range(int(p2[0]),int(p2[1])+1)]
    for i in range(len(p1)):
        if p1[i] in p2:
            newTotal += 1
            break
print(newTotal)
          
          
