x, y, z = float(input("Input three numbers:\n")), float(input()), float(input())

a1 = min(x, y, z)
a3 = max(x, y, z)

Average = (x + y + z) / 3
d1 = abs(x - Average)
d2 = abs(y - Average)
d3 = abs(z - Average)

middle = (min(d1, d2, d3) + Average)

if middle == x or middle == y or middle == z:
    a2 = int(middle)
else:
    middle = (-1 * min(d1, d2, d3)) + Average
    a2 = middle

print("Numbers in sorted order: ", a1, a2, a3)
