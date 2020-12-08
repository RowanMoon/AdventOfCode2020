import time

start_time = time.perf_counter_ns()
x = []

f = open("input.txt", "r")
for i in f.readlines():
    op = i.split(" ")[0]
    offset = i.split(" ")[1]
    x.append((op,int(offset.strip())))
f.close()



def problem1():
    acc = 0
    executed = []
    pointer = 0
    while(1):
        if(pointer in executed):
            return acc
        operation = x[pointer][0]
        data = x[pointer][1]
        if operation == "nop":
            executed.append(pointer)
            pointer+= 1
        elif operation == "acc":
            acc += data
            executed.append(pointer)
            pointer+=1
        else:
            executed.append(pointer)
            pointer+=data


def followThrough(pointer, acc):
    executed = []
    while(1):
        try:
            if(pointer in executed):
                return (False,0)
            operation = x[pointer][0]
            data = x[pointer][1]
            if operation == "nop":
                executed.append(pointer)
                pointer+= 1
            elif operation == "acc":
                acc += data
                executed.append(pointer)
                pointer+=1
            else:
                executed.append(pointer)
                pointer+=data
        except Exception as e:
            return (True,acc)
            
#BRUTE FORCE THE FUCKERs

def problem2():
    acc = 0
    pointer = 0
    while(1):
        try:
            operation = x[pointer][0]
            data = x[pointer][1]
            if operation == "nop":
                n = followThrough(pointer+data, acc)
                if(n[0]):
                    return n[1]
                pointer+= 1
            elif operation == "acc":
                acc += data
                pointer+=1
            else:
                n = followThrough(pointer+1, acc)
                if(n[0]):
                    return n[1]
                pointer+=data
        except Exception as e:
            return acc
        
        
        
p1 = problem1()
p2 = problem2()

print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')
print("Problem1: ",p1)
print("Problem 2: ",p2)