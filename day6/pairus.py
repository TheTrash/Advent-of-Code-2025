# PART 2

mat = []
with open('input.txt', 'r') as f:
 for line in f.readlines():
  mat.append(line)



operation = ""
arr_tmp = []
res = 0
for i in range(len(mat[0])):
    #print("I ", i )
    #print(" " , mat[i], " le ", len(mat[i]))

    tmp = ""
    for j in range(5):
        #print("here  ", mat[j][i])
        if mat[j][i] != " ":
            if mat[j][i] == "+":
                operation = "+"
            elif mat[j][i] == "*":
                operation = "*"
            else:
                tmp += mat[j][i]

    if tmp == "" or mat[j][i] == "\n":
        res_tmp_m = 1
        res_tmp_s = 0
        #print(arr_tmp)
        #print("operation ", operation)
        for e in arr_tmp:
            if operation == "*":
                res_tmp_m *= int(e)
            if operation == "+":
                res_tmp_s += int(e) 
        #print(res_tmp_m if operation == "*" else  res_tmp_s)
        res += res_tmp_m if operation == "*" else  res_tmp_s

        arr_tmp = []

    else:
        arr_tmp.append(tmp)
        tmp = ""

print(res)