x = []
y = {}
f = open("input.txt", "r")
for i in f.readlines():
    x.append(i.strip("\n"))
    

    
def processLine(st):
    a = st.split(" contain ")
    key = a[0][:-5]
    print(key)
    outData = []
    data = a[1]
    print(data)
    if data == "no other bags.":
        outData.append((0,""))
    else:
        data2 = data.split(", ")
        print(data2)


print(x)

for i in x:
    processLine(i)
