def triangular_mf(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif x == b:
        return 1.0
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

a = 20
b = 30
c = 40

temperature = float(input("Enter temperature in Celsius: "))
membership = triangular_mf(temperature, a, b, c)

print("Temperature:", temperature, "°C")
print("Warm Membership Value:", round(membership, 2))

# Input: Enter temperature in Celsius.
# Example: 25 -> 0.5, 30 -> 1.0, 35 -> 0.5, 45 -> 0.0.
# Run: python exp-exp9-fuzzy-membership-functions.py
