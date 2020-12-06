import time

start_time = time.perf_counter_ns()
x = []
x2 = []
y = ""
p = []
f = open("input.txt", "r")
for i in f.readlines():
    if i == "\n":
        x.append(y)
        x2.append(p)
        p=[]
        y = ""
    else:
        y = y + i.strip("\n")
        p.append(i.strip("\n"))
x.append(y)
x2.append(p)
p=[]
y = ""
    
    
def processLine(b):
    c = set(b)
    return c
    
    
def problem1():
    total = 0
    for i in x:
        total += len(processLine(i))
    return total

def processLine2(b):
    out = ""
    out2 = ""
    xLen = len(b)
    for i in b:
        out = out + i
    for i in out:
        if out.count(i) == xLen:
            out2 = out2 + i
    return set(out2)
    
def problem2():
    total = 0
    for i in x2:
        total += len(processLine2(i))
    return total
    
p1 = problem1()
p2 = problem2()

print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')

print("Problem 1: ",p1)
print("Problem 2: ",p2)