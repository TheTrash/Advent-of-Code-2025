def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp


def window(mat,y,x):
    tmp = ""
    le_x = len(mat[0])-1
    le_y = len(mat)-1
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            #print( i,j )
            if x == j and y == i:
                tmp += " x"
            elif ( 0 <= i <= le_y) and ( 0 <= j <= le_x ):
                tmp += " "+ mat[i][j]
                
        tmp += "\n"
    #print(tmp)
    return(tmp)




if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    mat = create_matrix(lines)
    le_x = len(mat[0])
    le_y = len(mat)
    res = 0
    valid = []
    for i in range(le_y):
        for j in range(le_x):
            if mat[j][i] == "@":
                wind = window(mat,j,i)
                c = wind.count('@')
                if c < 4:
                    valid.append((j,i))
                    res+=1
    print(res)

#for e in valid:
#    mat[e[0]][e[1]] = "x"

#for e in mat:
#    print(e)