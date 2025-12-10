# PART 1

import math

def euclidean_distance(p1, p2):

    return math.sqrt(
        (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
    )




lines = open("input.txt").read().splitlines()

points = []
circuits = {}
for e in lines:
    points.append(tuple([int(t) for t in e.split(",")]))

distances = []


for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append((i, j, euclidean_distance(points[i],points[j])))


distances.sort(key=lambda t: t[2])


circuits = []
connection = 10

## together the 1000 pairs of
for p1,p2, _ in distances[:]:
    added = False
    no_conn = False
    print(p1, p2, circuits)
    for i in range(len(circuits)):
        circuit = circuits[i]
        if p1 in circuit:
            #p1 è nel circuito quindi controllo se c'è anche p2
            if p2 in circuit:
                ## entrambi i punti sono aggiunti
                no_conn = True
                pass
            else:
                added = True
                # se p2 non è nel circuito aggiungo p2 al circuito
                # poi devo controllare se c'è qualche circuito che contiene p2 e nel caso unire p1 e p2
                for u in range(i+1,len(circuits)):
                    if p2 in circuits[u]:
                        circuit += circuits[u]
                        circuits[u] = []
                        break
                
                if p2 not in circuit: circuit.append(p2)
        else:
            # qui vuol dire che p1 non è nel circuito, controllo il successivo
            if p2 in circuit:
                added = True
                for u in range(i+1,len(circuits)):
                    if p1 in circuits[u]:
                        circuit += circuits[u]
                        circuits[u] = []
                        break
                if p1 not in circuit: circuit.append(p1)
            pass
    clear = []
    for i in range(len(circuits)):
        if circuits[i] == []:
            clear.append(i)
    for cl in clear:
        circuits.pop(cl)

    if not added and no_conn == False:
        circuits.append([p1,p2])
        #connection -=1
    print(p1, p2, circuits)

    
print(circuits)

circuits.sort(key=len, reverse=True)

res = len(circuits[0]) *  len(circuits[1]) *  len(circuits[2])
print(res)