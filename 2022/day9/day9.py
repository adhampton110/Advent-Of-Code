moves = []
with open("sample.txt") as source:
    for l in source:
        l = l.strip("\n")
        l = l.split()
        l[1] = int(l[1])
        moves.append(l)

class Rope:
    def __init__(self,startX,startY):
        self.currentHead = [startX,startY]
        self.currentTail = [startX,startY]
        self.prevHead = [startX,startY]
        self.visited = []
        self.tails = [Rope,Rope,Rope,Rope,Rope,Rope,Rope,Rope,Rope]

    def follow(self):
        if abs(self.currentHead[0]-self.currentTail[0]) > 1:
            return True
        if abs(self.currentHead[1]-self.currentTail[1]) > 1:
            return True
        return False

    def move(self,d):
        self.prevHead = (self.currentHead[0],self.currentHead[1])
        if d == "U":
            self.currentHead[1] += 1
        if d == "L":
            self.currentHead[0] -= 1
        if d == "D":
            self.currentHead[1] -= 1
        if d == "R":
            self.currentHead[0] += 1
        if self.follow():
            self.currentTail = self.prevHead
        if self.currentTail not in self.visited:
                self.visited.append(self.currentTail)

    def advancedMove(self,d):
        if d == "U":
            self.currentHead[1] += 1
        if d == "L":
            self.currentHead[0] -= 1
        if d == "D":
            self.currentHead[1] -= 1
        if d == "R":
            self.currentHead[0] += 1
        if self.follow():
            self.prevRope.currentHead = self.prevHead
            self.currentTail = self.prevHead
        if self.currentTail not in self.visited:
                self.visited.append(self.currentTail)

    def partOneAnswer(self):     
        return len(self.visited)

    def partTwoAnswer(self):
        return len(self.visited)-9

    def getVisited(self):
        return self.visited
            


r = Rope(0,0)
for d,i in moves:
    for j in range(i):
        r.move(d)
print("Part one answer:",r.partOneAnswer())
print(r.getVisited())
print("Part two answer:",r.partTwoAnswer())
