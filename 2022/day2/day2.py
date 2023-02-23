rounds = []
score = 0
with open("input.txt") as source:
    for line in source:
        line = line.strip("\n")
        line = line.split()
        rounds.append(line)

for match in rounds:
    if match[1] == "X":
        score += 1
        if match[0] == "C":
            score += 6
        if match[0] == "A":
            score += 3
    if match[1] == "Y":
        score+= 2
        if match[0] == "A":
            score += 6
        if match[0] == "B":
            score += 3
    if match[1] == "Z":
        score += 3
        if match[0] == "B":
            score += 6
        if match[0] == "C":
            score += 3

print(score)



score = 0 
for match in rounds:
    #lose
    if match[1] == "X":
        if match[0] == "A":
            score += 3
        elif match[0] == "B":
            score += 1
        else:
            score += 2
            #draw
    if match[1] == "Y":
        score+= 3
        if match[0] == "A":
            score += 1
        elif match[0] == "B":
            score += 2
        else:
            score += 3
    #win                
    if match[1] == "Z":
        score += 6
        if match[0] == "A":
            score += 2
        elif match[0] == "B":
            score += 3
        else:
            score += 1
print(score)
