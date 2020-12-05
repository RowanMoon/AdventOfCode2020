import time
start_time = time.perf_counter_ns()
y = []
z = []
zz = {}
import re


f = open("input.txt","r")

for i in f.readlines():
    if(i=='\n'):
        for ii in z:
            for iii in ii.split(" "):
                v = iii.split(":")
                key = v[0]
                data = v[1]
                zz[key] = data
        y.append(zz)
        zz = {}
        z = []
    else:
        z.append(i.strip("\n").strip(" "))

check = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eye = ['amb','blu','brn','gry','grn','hzl','oth']
b = []
  

def checker(dic):
    for c in check:
        if c in dic:
            k = 2
        else:
            return False
    return True

for i in y:
    if (checker(i.keys()) == True):
        b.append(i)  

def problem1():
    count = 0
    for i in y:
        if(checker(i.keys()) == True):
            count+=1
    return count
    
    
def problem2():
    count = 0
    for i in b:
        if(isValid(i)):
            count+=1
    return count
        
    
def isValid(dic):
    try:
        byr = int(dic['byr'])
        iyr = int(dic['iyr'])
        eyr = int(dic['eyr'])
        hgt = dic['hgt']
        hcl = dic['hcl']
        ecl = dic['ecl']
        pid = dic['pid']
        if(byr >= 1920 and byr <= 2002):
            #print("birth")
            if(iyr >= 2010 and iyr <= 2020):
                #print("issue")
                if(eyr >= 2020 and eyr <= 2030):
                    #print("expiration")
                    if('cm' in hgt):
                        #print("cm")
                        u = int(hgt.split("cm")[0])
                        if(u>=150 and u<=193):
                            #print("height")
                            if(hcl[0] == '#'):
                                #print("starts with #")
                                #print(hcl)
                                if(re.search("\A[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]",hcl[1:])!=None and len(hcl[1:])==6):
                                    #print("hex")
                                    for l in eye:
                                        if(ecl == l):
                                            #print("eye")
                                            if(re.search("\A[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",pid)!=None and len(pid)==9):
                                                #print("passport id")
                                                return True
                    elif('in' in hgt):
                        u = int(hgt.split("in")[0])
                        if(u>=59 and u<=76):
                            if(hcl[0] == '#'):
                                if(re.search("\A[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]",hcl[1:])!=None and len(hcl[1:])==6):
                                    for l in eye:
                                        if(ecl == l):
                                            if(re.search("\A[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",pid)!=None and len(pid)==9):
                                                return True
        return False
    except Exception as e:
        return False
xx = problem1()
yy = problem2()
print(f'time taken: {(time.perf_counter_ns() - start_time)/1000000}ms')

print("Problem 1: ",xx)
print("Problem 2: ",yy)