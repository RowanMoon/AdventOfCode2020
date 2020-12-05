import time

start_time = time.perf_counter_ns()
x = []
u = 73
f = open("input.txt", "r")
for i in f.readlines():
    b = i.strip("\n")
    x.append(b * u)
    y = len(b)
x.append("a" * y * u)
x.append("a" * y * u)
def problem1():
    xPos = 0
    yPos = 0
    numTreesHit = 0
    while(x[yPos][xPos]!="a"):
        xPos += 3
        yPos += 1
        if(x[yPos][xPos] == "#"):
            numTreesHit+=1
    return numTreesHit
routes = [(1,1),(5,1),(7,1),(1,2)]
def problem2():
    totalTreesHit = 1
    for i in routes:
        xPos = 0
        yPos = 0
        numTreesHit = 0
        while(x[yPos][xPos]!="a"):
            xPos += i[0]
            yPos += i[1]
            if(x[yPos][xPos] == "#"):
                numTreesHit+=1
        totalTreesHit *= numTreesHit
    return totalTreesHit
xx = problem1()
y = problem2() * xx
print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')
print(xx)
print(y)