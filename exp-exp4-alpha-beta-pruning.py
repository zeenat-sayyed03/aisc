import math

def alphabeta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -math.inf
        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
result = alphabeta(0, 0, True, values, -math.inf, math.inf)
print("Optimal Value:", result)

# Input: No input required.
# Leaf values: [3, 5, 6, 9, 1, 2, 0, -1]
# Expected output: Optimal Value: 5
# Run: python exp-exp4-alpha-beta-pruning.py
