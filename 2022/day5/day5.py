#input processing
#personal input
'''
stacks = [
    [], #stack 0
    ["F","H","B","V","R","Q","D","P"], #stack 1
    ["L","D","Z","Q","W","V"], #stack 2
    ["H","L","Z","Q","G","R","P","C"], #stack 3
    ["R","D","H","F","J","V","B"], #stack 4
    ["Z","W","L","C"], #stack 5
    ["J","R","P","N","T","G","V","M"], #stack 6
    ["J","R","L","V","M","B","S"], #stack 7
    ["D","P","J"], #stack 8
    ["D","C","N","W","V"] #stack 9 
]
'''
#sample input
stacks = [
    [],
    ["Z","N"],
    ["M","C","D"],
    ["P"]
]
operations = []
with open("sample.txt") as source:
    for line in source:
        line = line.strip("\n")
        if "move" in line:
            rules = [int(char) for char in line if char.isnumeric()]
            operations.append(rules)


for move in operations:
    iterations = move[0]
    base = stacks[move[1]]
    goal = stacks[move[2]]
    for i in range(iterations):
        if base != []:
            goal.append(base.pop())

partOneAnswer = ""
for stack in stacks:
    if stack != []:
        partOneAnswer += stack[-1]
print(partOneAnswer)
