#PART 1

c=0
lines = open("test.txt").read().splitlines()

for line in lines:
    myList = [int(c) for c in list(line.replace("\n",""))]
    index = 0
    max_1 = 0
    max_2 = 0
    for e,i in zip(myList[:-1],range(len(myList[:-1]))):
        if max_1 < e:
            max_1 = e
            index = i
    print(max_1, index)
    for e,i in zip(myList[index+1:],range(len(myList[index+1:]))):
        if max_2 < e:
            max_2 = e
            index = i
    print(max_1, max_2)