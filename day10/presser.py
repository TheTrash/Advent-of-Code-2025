import re
lines = open("test.txt").read().splitlines()

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

def rec(panel, button):
    new_panel = press(panel, button)
    if new_panel == panel_goal:
        return True
    else:
        pass

res = 0
for s in lines:
    # 1. panel_goal: prendo quello che c'è tra [ e ]
    panel_goal = list(re.search(r'\[([.#]+)\]', s).group(1))
    # 2. buttons: prendo tutte le parentesi tonde ( ... )
    buttons_raw = re.findall(r'\(([^)]*)\)', s)
    buttons = []
    for b in buttons_raw:
        nums = [int(x) for x in b.split(',') if x]
        # se c'è un solo numero: int semplice (3)
        # se ce ne sono due: tupla (1, 3)
        buttons.append(tuple(nums))

    # 3. jolts: prendo quello che c'è tra { e } e lo trasformo in set di int
    jolts = {int(x) for x in re.search(r'\{([^}]*)\}', s).group(1).split(',')}




    panel = ["."]* (len(panel_goal))
    print(panel, panel_goal, buttons)
    pressed = []
    for i in range(len(buttons)):
        combination = []
        panel = ["."]* (len(panel_goal))
        #print("new loop ------ ")
        for button in buttons[i:]:
            panel = press(panel,button)
            combination.append(button)
            if panel == panel_goal:
                print(combination, panel, panel_goal, panel == panel_goal)
                pressed.append((combination, panel, len(combination)))
                break
        #print(" ------ ")


    pressed.sort(key=lambda t: t[2])
    print(pressed[0][2])
    res += pressed[0][2]