lines = open("input.txt").read().splitlines()


couples = lines[0].split(",")
#print(couples)




def tmp(number):
    n_string = str(number)
    if len(n_string)%2 == 1:
        return False
    else:
        return n_string[0:len(n_string)//2] == n_string[len(n_string)//2:]
    



res = 0
for c in couples:
    t= c.split("-")
    #print(t[0], t[1])
    for e in range(int(t[0]),int(t[1])+1,1):
        if tmp(e):
            res += e



print(res)
