x = []
f = open("input.txt", "r")
for i in f.readlines():
    x.append(i.strip("\n"))
    
    
def process(inp):
    row = inp[:7]
    col = inp[7:]
    foundRow = 0
    foundCol = 0
    l = 0
    b = 128
    y = [*range(b)]
    for i in row:
        if i == "F":
            b = midpoint(b, l)
            y = [*range(l,b)]
        elif i == "B":
            l = midpoint(b, l)
            y = [*range(l,b)] 
    l = 0
    b = 8
    v = [*range(b)]
    for i in col:
        if i == "R":
            l = midpoint(b, l)
            v = [*range(l,b)]
        elif i == "L":
            b = midpoint(b, l)
            v = [*range(l,b)]
    return (y[0], v[0])
    

def midpoint(x,y):
    return int((x + y) / 2)

def problem1():
    highest = 0
    for i in x:
        row, col = process(i)
        seatID = (row * 8) + col
        if seatID > highest:
            highest = seatID
    return highest


def getList():
    yy = []
    for i in x:
        row, col = process(i)
        seatID = (row * 8) + col
        yy.append(seatID)
    yy.sort()
    return yy

def problem2():
    yy = getList()
    last = yy[0]
    for i in yy:
        if i == last:
            continue
        elif last == i - 1:
            last = i
            continue
        else:
            return i - 1
    
print(problem1())
print(problem2())
