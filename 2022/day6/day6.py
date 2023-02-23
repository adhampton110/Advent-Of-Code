def uniqueCheck(string):
    sortedString = sorted(string)
    for i in range(len(sortedString)-1):
        if sortedString[i] == sortedString[i+1]:
            return False
    return True

buffer = ""
with open("input.txt") as source:
    buffer = source.read()

for i in range(len(buffer)):
    marker = buffer[i:i+4]
    result = uniqueCheck(marker)
    if result:
        print(i+4)
        break

for i in range(len(buffer)):
    marker = buffer[i:i+14]
    result = uniqueCheck(marker)
    if result:
        print(i+14)
        break
    
    
