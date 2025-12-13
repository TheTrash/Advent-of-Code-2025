# PART 2
from functools import lru_cache
lines = open("input.txt").read().splitlines()

@lru_cache
def DFS(node, arrival):
    if node == arrival:
        return 1
    total_path = 0

    for ne in nodes[node]:
        p = DFS(ne, arrival)
        total_path +=p

    return total_path
    
       

nodes = {}
for line in lines:
    line = line.split(" ")
    nodes[line[0].replace(":","")] = line[1:]

nodes["out"] = []


a1 = DFS("svr","fft")
print(a1)
b1 = DFS("fft","dac")
print(b1)
c1 = DFS("dac","out")
print(c1)
print("--")

a2 = DFS("svr","dac")
print(a2)
b2 = DFS("dac","fft")
print(b2)
c2 = DFS("fft","out")
print(c2)
print("--")

print((a1*b1*c1)+(a2*b2*c2))