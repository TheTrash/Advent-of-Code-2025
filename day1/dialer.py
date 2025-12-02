tmp = 50
c = 0
t = 0
with open('test.txt') as file:
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
        #print(tmp)
        if 0 < tmp < 100:
            print("pass to 0")
            t+=1


        tmp=tmp%100
        print("rotate ", e, " into ", tmp)
        tmp=tmp%100
        if tmp == 0:
            c+=1

print("part_1", c)
print("part_2",c+t)