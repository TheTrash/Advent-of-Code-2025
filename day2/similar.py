

def tmp(number, split= 2):
    n_string = str(number)
    le = len(n_string)

    if n_string[0:le//2] == n_string[le//2:]:
        return True

    tmp = n_string[0:split]
    for e in range(0,le,split):
        if tmp != n_string[e:e+split]:
            return False

    return True

def test(number):
    number = str(number)
    for e in range(1,len(number)):
        if tmp(number,e) == True:
            return True


if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    couples = lines[0].split(",")
    res = 0
    for c in couples:
        t = c.split("-")
        for e in range(int(t[0]),int(t[1])+1,1):
            if test(e):
                res += e

    print(res)