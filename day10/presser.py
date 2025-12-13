# PART 1

import re
from itertools import product
lines = open("input.txt").read().splitlines()

def press(panel,button):
    # in input prendo 
    # "...." (pos) 
    # "...." (pos, pos, ..)
    #print(type(button))
    #print(panel, button)
    for e in button:
        if panel[e] == '.':
            panel[e] = "#"
        else:
            panel[e] = "."

    return panel

res = 0
for s in lines:
    # 1. panel_goal: prendo quello che c'è tra [ e ]
    panel_goal = list(re.search(r'\[([.#]+)\]', s).group(1))
    # 2. buttons: prendo tutte le parentesi tonde ( ... )
    buttons_raw = re.findall(r'\(([^)]*)\)', s)
    buttons = []
    for b in buttons_raw:
        nums = [int(x) for x in b.split(',') if x]
        # se c'è un solo numero: int semplice (3,)

        buttons.append(tuple(nums))

    # 3. jolts: prendo quello che c'è tra { e } e lo trasformo in set di int
    jolts = {int(x) for x in re.search(r'\{([^}]*)\}', s).group(1).split(',')}

    panel = ["."]* (len(panel_goal))
    print(panel, panel_goal, buttons)
    pressed = []

    find = False
    for i in range(1, len(buttons) + 1):
        for sol in product(buttons, repeat=i):
            panel = ["."]* (len(panel_goal))
            for button in sol:    
                panel = press(panel,button)
                if panel == panel_goal:
                    pressed.append(sol)
                    print(sol)
                    res += len(sol)
                    find = True
                    break
            if find == True:
                break
        if find == True:
            break


print(res)