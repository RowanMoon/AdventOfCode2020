import time

start_time = time.perf_counter_ns()
from operator import xor
x = []
f = open("input.txt", "r")
for i in f.readlines():
    x.append(i)

def checkPasswords():
    total = 0
    for i in x:
        bounds = i.split(" ")[0]
        min = int(bounds.split("-")[0])
        max = int(bounds.split("-")[1])
        char = i.split(" ")[1].split(":")[0]
        passW = i.split(" ")[2]
        numInstances = passW.count(char)
        if(numInstances >= min and numInstances <= max):
            total += 1
        
    return total


def checkPasswords2():
    total = 0
    for i in x:
        bounds = i.split(" ")[0]
        min = int(bounds.split("-")[0])
        max = int(bounds.split("-")[1])
        char = i.split(" ")[1].split(":")[0]
        passW = i.split(" ")[2]
        if(xor(passW[min-1] == char,passW[max-1] == char)):
            total += 1
    return total

y = checkPasswords()
z = checkPasswords2()
print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')  