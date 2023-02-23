#parse layout
layout = []
with open("input.txt") as source:
    for l in source:
        l = l.strip("\n")
        layout.append([int(i) for i in l])

#part 1
def visible(y,x):
    left = right = up = down = True
    leftScore = rightScore = upScore = downScore = 0 
    #left check
    for index in range(0,x):
        if layout[y][index] >= layout[y][x]:
            left = False
    #right check
    for index in range(x+1,len(layout[y])):
        if layout[y][index] >= layout[y][x]:
            right = False      
    #up check
    for index in range(0,y):
        col = layout[index]
        if col[x] >= layout[y][x]:
            up = False
    #down check
    for index in range(y+1,len(layout)):
        col = layout[index]
        if col[x] >= layout[y][x]:
            down = False
    l = [left,right,up,down]
    if any(l):
        return True
    else:
        return False
#part 2
def treeScore(y,x):
    left = right = up = down = True
    leftScore = rightScore = upScore = downScore = 0
    #left check
    for index in reversed(range(0,x)):
        if left:
            leftScore += 1
            if layout[y][index] >= layout[y][x]:
                left = False
    #right check
    for index in range(x+1,len(layout[y])):
        if right:
            rightScore += 1
            if layout[y][index] >= layout[y][x]:
                right = False          
    #up check
    for index in reversed(range(0,y)):
        col = layout[index]
        if up:
            upScore += 1
            if col[x] >= layout[y][x]:
                up = False
    #down check
    for index in range(y+1,len(layout)):
        col = layout[index]
        if down:
            downScore += 1
            if col[x] >= layout[y][x]:
                down = False
    return leftScore * rightScore * upScore * downScore

 
scores = []   
total = 0
total += len(layout[0]) * 2 #first & last edges
total += len(layout)*2-4 #edges for each row
for i in range(1,len(layout)-1):
    row = layout[i]
    for j in range(1,len(row)-1):
        scores.append(treeScore(i,j))
        if visible(i,j):
            total += 1
print("Part one answer:",total)
print("Part two answer:",max(scores))
