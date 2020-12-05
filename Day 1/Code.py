import time
start_time = time.perf_counter_ns()
x = []
f = open("input.txt", "r")
for i in f.readlines():
    x.append(int(i))

x.sort()

def check_2020():
    for i in range(int(len(x))):
        y = x[i]
        checkNum = 2020 - y
        for ii in range(i,len(x)):
            if(checkNum == x[ii]):
                return (y * x[ii])
            
def check_2020_2():
    for i in range(len(x)):
        num1 = x[i]
        for ii in range(len(x)):
            num2 = x[ii]
            num12 = num1 + num2
            for iii in range(len(x)):
                num3 = x[iii]
                if(num12 + num3 ==2020):
                    return(num1 * num2 * num3)
                
b = check_2020()

c = check_2020_2()

print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')  