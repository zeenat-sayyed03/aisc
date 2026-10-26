from collections import deque

CAP_A = 4
CAP_B = 3

def next_states(state):
    a, b = state
    states = [(CAP_A, b), (a, CAP_B), (0, b), (a, 0)]
    t = min(a, CAP_B - b)
    states.append((a - t, b + t))
    t = min(b, CAP_A - a)
    states.append((a + t, b - t))
    return list(dict.fromkeys(states))

def bfs():
    start = (0, 0)
    goal = (2, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for nxt in next_states(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

solution = bfs()
print("Solution Path:")
if solution:
    for state in solution:
        print(state)
else:
    print("No solution found.")

# Input: No input required.
# Goal state: (2, 0), meaning Jug A contains 2 litres.
# Run: python exp-exp2-water-jug-bfs.py
