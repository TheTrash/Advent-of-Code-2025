# PART2




if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    ranges = []
    res = 0
    
    for e in lines:
        if e == "":
            break
        tmp = [ int(c) for c in e.split("-")]
        ranges.append((tmp[0], tmp[1]))
    
    # ordino gli intervalli così devo solo controllare
    # che siano maggiori o uguali perché so per certo che non c'è niente 
    # prima
    ranges = sorted(ranges, reverse=False)

    big_range = [c for c in ranges.pop(0)]
    for i,e in zip(range(len(ranges)),ranges):
        # se l'ultima frontiera è minore del nuovo numero, sono sicuramente davanti ad un nuovo intervallo
        if big_range[len(big_range)-1] < e[0]:
            big_range.append(e[0])
            big_range.append(e[1])

        # se la frontiera è maggiore del primo numero dell'intervallo E il secondo numero è più grande è un intervallo che parte 
        # dentro quello vecchio e finisce dopo, aggiorno la frontiera.
        if big_range[len(big_range)-1] >= e[0] and big_range[len(big_range)-1] < e[1]:
            big_range.pop()
            big_range.append(e[1])
        
    #print(big_range)

    for e in range(0,len(big_range)-1,2):
        #print(big_range[e], big_range[e+1])
        res += big_range[e+1] - big_range[e] +1

    print(res)


