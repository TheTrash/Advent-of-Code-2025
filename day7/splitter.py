def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    mat = create_matrix(lines)
    le_x = len(mat[0])
    le_y = len(mat)

    # Creando una matrice di supporto vuota per contare 
    # quante volte passa il laser
    mat2 = create_matrix(lines)
    for i in range(le_y):
        for j in range(le_x):
            if ( 0 <= i <= le_y) and ( 0 <= j <= le_x ):
                mat2[i][j] = 0


    res = 0
    valid = []
    t = ""


    for i in range(le_y):
        for j in range(le_x):
            if ( 0 <= i <= le_y) and ( 0 <= j <= le_x ):
                if mat[i][j]  == 'S' and mat[i-1][j]  == ".":
                    print("start!")
                    mat[i+1][j] = "|"
                    mat2[i+1][j] = 1
                if mat[i][j]  == "^" and mat[i-1][j]  == "|" :
                    # spawno il laser a destra e sinistra
                    print("split")

                    #sinistra
                    mat[i][j-1] = "|"
                    mat2[i][j-1] = mat2[i][j-1] + mat2[i-1][j] #+ mat2[i-1][j-1] qui non sommo il laser top perché lo sommo sotto
                

                    # destra
                    mat[i][j+1] = "|"
                    mat2[i][j+1] = mat2[i][j+1] + mat2[i-1][j] + mat2[i-1][j+1]

                if mat[i][j] == "." and mat[i-1][j]  == "|" :
                    print("laser propagation")
                    # propago il laser sulla cella
                    mat[i][j] = "|"
                    mat2[i][j] = mat2[i-1][j]

    for e in mat:
        print(e)

    print(res)

    print("---------------SECOND PART----------------")
    res2 = 0
    for e,z in zip(mat,mat2):
        print(e, " ", z)
    print(sum(mat2[-1]))

