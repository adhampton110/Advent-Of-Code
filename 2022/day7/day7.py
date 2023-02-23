#parse input
moves = []
with open("sample.txt") as source:
    for line in source:
        line = (line.strip("\n") and line.strip("$")).split()
        if line[0] == "ls" or line[0] == "dir" in line:
            pass
        else:
            moves.append(line)
            
#part 1
files = {}
filePath = []
for i in range(len(moves)):
    m = moves[i]
    c = m[0]
    if c == "cd":
        if ".." in m:
            filePath.pop()
        else:
            filePath.append(i)
            if i not in files.keys():
                files[i] = 0 
    if c.isnumeric():
        size = int(m[0])
        for d in filePath:
            files[d] += size

result = sum([i for i in files.values() if i<=100000])
print("Part One Answer:",result)

#part 2
avail = 70000000 - max(files.values())
result2 = min([i for i in files.values() if i+avail>=30000000])
print("Part Two Answer:",result2)
