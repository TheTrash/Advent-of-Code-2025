import math

tmp = 50
n_tmp = 50
c = 0
t = 0

def add(tmp):
    if tmp == 99:
        return 0
    else:
        return tmp+1

def sub(tmp):
    if tmp == 0:
        return 99
    else:
        return tmp-1


lines = open("input.txt").read().splitlines()
for e in lines:
        #print line,  # The comma to suppress the extra new line char
    if e[0] == 'L':
        for step in range(int(e[1:])):
            tmp = sub(tmp)
            if tmp == 0:
                c+=1

    elif e[0] == 'R':
        for step in range(int(e[1:])):
            tmp = add(tmp)
            if tmp == 0:
                c+=1


print("part_1", c)
print("part_2", c+t)