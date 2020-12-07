import time



start_time = time.perf_counter_ns()
x = []
y = {}
f = open("input.txt", "r")
for i in f.readlines():
    x.append(i.strip("\n"))
    

    
def processLine(st):
    a = st.split(" contain ")
    key = a[0][:-5]
    outData = []
    data = a[1]
    if data == "no other bags.":
        outData.append((0,"no other bags."))
    else:
        data2 = data.split(", ")
        for ii in data2:
            h = ii.split(" bag")[0][2:]
            num = ii.split(" ")[0]
            outData.append((num,h))
    return (key,outData)
   
for i in x:
    key, data = processLine(i)
    y[key] = data
    
def check(bag):
    result = False
    for i in y[bag]:
        b = i[1]
        if b == "shiny gold":
            result = True
        elif b == "no other bags.":
            result = False
        else:
            result = check(b)
        if result:
            return result
        
def problem1():
    count = 0
    for i in y:
        j = check(i)
        if j == True:
            count += 1
    return count

def check2(h):
    total = 0
    for i in y[h]:
        b = i[1]
        if b == "no other bags.":
            return 0
        else:
            total += int(i[0]) + (int(i[0]) * check2(b))
    return total
    
k = check2('shiny gold')       
l = problem1()     

print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')
print("Problem 1: ", l)
print("Problem 2: ", k)

