# PART1




if __name__ == "__main__":
    lines = open("input.txt").read().splitlines()
    input_find = False
    ranges = []
    res =0
    for e in lines:
        if e == "":
            input_find = True

        if input_find == False:
            ranges.append([ int(c) for c in e.split("-")])
        elif e != "":
            for range in ranges:
                if range[0] <= int(e) <= range[1]:
                    print(f"trovato {e} in {range}")
                    res+= 1
                    break 


    
    print(res)