# PART 1

def square_area(x1,y1,x2,y2):
    #print(x1,y1, " - " ,x2,y2, ":", (abs(x1-x2)+1)*(abs(y1-y2)+1))
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)


lines = open("input.txt").read().splitlines()

lines = [[int(x) for x in line.split(",")] for line in lines]

areas = []

for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            x1,y1 = ( lines[i][0], lines[i][1])
            x2,y2 = ( lines[j][0], lines[j][1])
            areas.append((i,j,square_area(x1,y1,x2,y2)))

areas.sort(key=lambda t: t[2], reverse=True)
print(areas[0])
