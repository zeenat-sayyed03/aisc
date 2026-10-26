import math
import random

def sigmoid(x):
    x = max(-500, min(500, x))
    return 1 / (1 + math.exp(-x))

def derivative(y):
    return y * (1 - y)

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 0]

random.seed(42)
wih = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
who = [random.uniform(-1, 1) for _ in range(2)]
bh = [0.0, 0.0]
bo = 0.0
lr = 0.5
epochs = 10000

for epoch in range(epochs):
    for inputs, target in zip(X, Y):
        hidden = [
            sigmoid(inputs[0] * wih[0][j] + inputs[1] * wih[1][j] + bh[j])
            for j in range(2)
        ]
        output = sigmoid(hidden[0] * who[0] + hidden[1] * who[1] + bo)
        error_out = (target - output) * derivative(output)
        error_hidden = [derivative(hidden[j]) * who[j] * error_out for j in range(2)]

        for j in range(2):
            who[j] += lr * error_out * hidden[j]
        bo += lr * error_out

        for j in range(2):
            wih[0][j] += lr * error_hidden[j] * inputs[0]
            wih[1][j] += lr * error_hidden[j] * inputs[1]
            bh[j] += lr * error_hidden[j]

print("XOR Gate Results")
for inputs, target in zip(X, Y):
    hidden = [
        sigmoid(inputs[0] * wih[0][j] + inputs[1] * wih[1][j] + bh[j])
        for j in range(2)
    ]
    output = sigmoid(hidden[0] * who[0] + hidden[1] * who[1] + bo)
    print(inputs, "Target:", target, "Output:", round(output, 3),
          "Predicted:", int(output >= 0.5))

# Input: No input required; XOR training data is predefined.
# Run: python exp-exp7-mlp-backpropagation-xor.py
