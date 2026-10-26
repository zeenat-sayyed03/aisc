POP_SIZE = 6
LENGTH = 5

def validate(ch):
    ch = ch.strip()
    if len(ch) != LENGTH or any(b not in "01" for b in ch):
        raise ValueError("Enter exactly 5 binary bits.")
    return ch

def fitness(ch):
    x = int(ch, 2)
    return x * x

def mutate(ch, pos):
    bits = list(ch)
    bits[pos - 1] = "1" if bits[pos - 1] == "0" else "0"
    return "".join(bits)

print("GENETIC ALGORITHM - ONE GENERATION")
population = []
for i in range(POP_SIZE):
    while True:
        try:
            ch = validate(input(f"Enter chromosome {i + 1}: "))
            population.append(ch)
            break
        except ValueError as e:
            print("Error:", e)

print("\nInitial Population")
for ch in population:
    print(ch, "Decimal:", int(ch, 2), "Fitness:", fitness(ch))

population.sort(key=fitness, reverse=True)
p1, p2 = population[:2]
print("\nSelected Parents")
print("Parent 1:", p1, "Fitness:", fitness(p1))
print("Parent 2:", p2, "Fitness:", fitness(p2))

while True:
    try:
        point = int(input("Enter crossover point (1-4): "))
        if 1 <= point <= 4:
            break
        print("Enter a point between 1 and 4.")
    except ValueError:
        print("Enter a valid integer.")

o1 = p1[:point] + p2[point:]
o2 = p2[:point] + p1[point:]
print("\nOffspring after Crossover")
print("Offspring 1:", o1)
print("Offspring 2:", o2)

print("\nMutation Options")
print("1. Mutate Offspring 1")
print("2. Mutate Offspring 2")
print("3. Mutate Both")
print("4. No Mutation")
while True:
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice in [1, 2, 3, 4]:
            break
        print("Choose 1, 2, 3 or 4.")
    except ValueError:
        print("Enter a valid integer.")

if choice in [1, 2, 3]:
    if choice in [1, 3]:
        while True:
            try:
                pos = int(input("Mutation position for Offspring 1 (1-5): "))
                if 1 <= pos <= 5:
                    o1 = mutate(o1, pos)
                    break
                print("Position must be between 1 and 5.")
            except ValueError:
                print("Enter a valid integer.")
    if choice in [2, 3]:
        while True:
            try:
                pos = int(input("Mutation position for Offspring 2 (1-5): "))
                if 1 <= pos <= 5:
                    o2 = mutate(o2, pos)
                    break
                print("Position must be between 1 and 5.")
            except ValueError:
                print("Enter a valid integer.")

print("\nFinal Offspring")
print(o1, "Fitness:", fitness(o1))
print(o2, "Fitness:", fitness(o2))
population = population[2:] + [o1, o2]
population.sort(key=fitness, reverse=True)

print("\nFinal Population")
for i, ch in enumerate(population, 1):
    print(i, ch, "Decimal:", int(ch, 2), "Fitness:", fitness(ch))
print("\nBest Chromosome:", population[0])
print("Best Fitness:", fitness(population[0]))

# Input:
# 1. Enter 6 chromosomes, each exactly 5 bits.
# 2. Enter crossover point (1-4).
# 3. Choose mutation option (1-4).
# 4. If needed, enter mutation positions (1-5).
# Run: python exp-exp5-genetic-algorithm.py
