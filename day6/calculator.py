# PART 1

mat = []
with open('input.txt', 'r') as f:
 for line in f.readlines():
  mat.append([ e for e in line.replace("\n","").split(" ") if e!= ""])

res = [ 1 ] * len(mat[0])
for i in range(len(mat)-1):
    print(len(mat[i]))
    le = len(mat[i])
    for j, e in enumerate(mat[i]):
        #print(mat[i][j])
        if i == 0:
            res[j] = int(mat[i][j])
        else:
            if mat[4][j] == "+":
                res[j] +=  int(mat[i][j])
            elif mat[4][j] == "*":
                res[j] *=  int(mat[i][j])

print(sum(res))