x = []

f = open("input.txt", "r")
for i in f.readlines():
    x.append(int(i.strip()))
    
    
def check(pointer):
    for i in range(pointer-25,pointer):
        for ii in range(i,pointer):
            if x[i] + x[ii] == x[pointer]:
                #print(x[i], " + ", x[ii], " = ", x[pointer])
                return True
    return False

def problem1():
    pointer = 25
    for i in range(pointer,len(x)):
        if (check(i) == False):
            return x[i]
            
weakness = problem1()


y = x
   
def problem2(target):
    for i in range(len(y)):
        total = 0
        for ii in range(i,len(y)):
            total+=y[ii]
            if total == target:
                print(i,ii)
                b = []
                for i in range(i,ii):
                    b.append(y[i])
                b.sort()
                return b[0] + b[len(b)-1]
            
print(problem2(weakness))
            
    