tmp = 50
c = 0
with open('input.txt') as file:
    for e in file:
        #print line,  # The comma to suppress the extra new line char
        if e[0] == 'L':
            #print( "sottrai", e[1:])
            tmp= tmp - int(e[1:])
        elif e[0] == 'R':
            #print("somma", e[1:])
            tmp= tmp + int(e[1:])
        else:
            pass

        #print("rotate ", e, " into ", tmp)
        tmp=tmp%100
        if tmp == 0:
            c+=1

print("part_1", c)
