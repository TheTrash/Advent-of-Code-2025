# PART 1
lines = open("test.txt").read().splitlines()

visit = 0

def DFS(node):
    global visit
    print(node)
    #visited.append(node)
    for ne in nodes[node]:
        if ne == "out": 
            visit +=1
        if ne not in visited and ne != "out":
            DFS(ne)

nodes = {}
for line in lines:
    line = line.split(" ")
    nodes[line[0].replace(":","")] = line[1:]

nodes["out"] = []
visited = []

DFS("you")

print(visit)
