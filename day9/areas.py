# PART 2 
# using a library for geometry shape
# asked to gpt the library
from shapely.geometry import Point, Polygon


def square_area(x1,y1,x2,y2):
    #print(x1,y1, " - " ,x2,y2, ":", (abs(x1-x2)+1)*(abs(y1-y2)+1))
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)


lines = open("input.txt").read().splitlines()

lines = [tuple(int(x) for x in line.split(",")) for line in lines]

areas = []

polygon = Polygon(lines)

for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            x1,y1 = ( lines[i][0], lines[i][1])
            x2,y2 = ( lines[j][0], lines[j][1])
            if polygon.covers(Polygon([(x1,y1),(x1,y2),(x2,y2),(x2,y1)])):
                areas.append((i,j,square_area(x1,y1,x2,y2)))

areas.sort(key=lambda t: t[2], reverse=True)
print(areas[0])
