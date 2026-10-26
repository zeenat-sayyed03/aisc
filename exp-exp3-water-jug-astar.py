from heapq import heappush, heappop

CAP_A = 4
CAP_B = 3
GOAL = 2

def heuristic(state):
    return abs(GOAL - state[0])

def successors(state):
    a, b = state
    states = [(CAP_A, b), (a, CAP_B), (0, b), (a, 0)]
    t = min(a, CAP_B - b)
    states.append((a - t, b + t))
    t = min(b, CAP_A - a)
    states.append((a + t, b - t))
    return list(dict.fromkeys(states))

def astar():
    start = (0, 0)
    pq = [(heuristic(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        if state[0] == GOAL:
            return path
        for nxt in successors(state):
            if nxt not in visited:
                new_g = g + 1
                heappush(pq, (new_g + heuristic(nxt), new_g, nxt, path + [nxt]))
    return None

solution = astar()
print("Solution Path:")
if solution:
    for state in solution:
        print(state)
else:
    print("No solution found.")

# Input: No input required.
# Jug capacities: A = 4 litres, B = 3 litres.
# Goal: Exactly 2 litres in Jug A.
# Run: python exp-exp3-water-jug-astar.py
