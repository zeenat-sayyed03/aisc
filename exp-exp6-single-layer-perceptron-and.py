X = [(0, 0), (0, 1), (1, 0), (1, 1)]
Y = [0, 0, 0, 1]

w1 = 0
w2 = 0
b = 0
learning_rate = 1

def activation(net):
    return 1 if net >= 0 else 0

for epoch in range(100):
    total_error = 0
    for (x1, x2), target in zip(X, Y):
        net = w1 * x1 + w2 * x2 + b
        output = activation(net)
        error = target - output
        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        b += learning_rate * error
        total_error += abs(error)
    if total_error == 0:
        print("Training completed at epoch", epoch + 1)
        break

print("\nAND Gate Results")
print("X1 X2 Target Output")
for (x1, x2), target in zip(X, Y):
    output = activation(w1 * x1 + w2 * x2 + b)
    print(x1, x2, target, output)
print("\nWeights:", w1, w2)
print("Bias:", b)

# Input: No input required; the AND truth table is predefined.
# Expected outputs: 0, 0, 0, 1.
# Run: python exp-exp6-single-layer-perceptron-and.py
