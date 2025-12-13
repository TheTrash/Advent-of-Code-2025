# PART 2

from ortools.sat.python import cp_model
import re
import time

lines = open("input.txt").read().splitlines()

sol = 0
start = time.perf_counter()
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
    jolts_goal = tuple([int(x) for x in re.search(r'\{([^}]*)\}', s).group(1).split(',')])

    

    dims = len(jolts_goal)
    m = len(buttons)
        # A is the resulting matrix
    A = [tuple(1 if d in btn else 0 for d in range(dims)) for btn in buttons]

    model = cp_model.CpModel()

        # constraint of not exceeding goal
    ub_global = max(jolts_goal) if jolts_goal else 0
    x = [model.NewIntVar(0, ub_global, f"x{i}") for i in range(m)]

    for d in range(dims):
        model.Add(sum(x[i] * A[i][d] for i in range(m)) == jolts_goal[d])

        # solve for min(sum(coeff))
    model.Minimize(sum(x))

    solver = cp_model.CpSolver()

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        print("NO SOLUTION")

    sol +=int(solver.ObjectiveValue())


elapsed = time.perf_counter() - start

print(f"Tempo: {elapsed:.6f} s")

print(sol)