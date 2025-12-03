#PART 2

c = [0] * 12
print(c, len(c))
lines = open("input.txt").read().splitlines()
res = 0
for line in lines:
    myList = [int(c) for c in list(line.replace("\n",""))]
    le = len(myList)+1
    
    l_index = -1
    for i in range(12):
        ma = 0
        #print(myList[l_index+1:le-(12-i)],range(l_index+1,le))
        for e, j in zip(myList[l_index+1:le-(12-i)],range(l_index+1,le)):
            if e > ma:
                ma = e
                l_index = j
        #print(l_index)
        c[i] = ma

    #print(c)
    #print(int("".join(map(str,c))))
    res += int("".join(map(str,c)))
print(res)