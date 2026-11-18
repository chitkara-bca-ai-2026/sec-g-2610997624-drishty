print("Pattern 1: Star Triangle")
print("-----------------------------------")
for r in range(1, 6):
    for c in range(r):
        print("*", end=" ")
    print()

print()

print("Pattern 2: Number Triangle")
print("-----------------------------------")
for r in range(1, 6):
    for c in range(1, r + 1):
        print(c, end=" ")
    print()

print()

print("Pattern 3: Inverted Star Triangle")
print("-----------------------------------")
for r in range(5, 0, -1):
    for c in range(r):
        print("*", end=" ")
    print()

print()

print("Pattern 4: Pyramid")
print("-----------------------------------")
n = 5
for row in range(1, n + 1):
    for col in range(n - row):
        print(" ", end=" ")
    for col in range(2 * row - 1):
        print("*", end=" ")
    print()