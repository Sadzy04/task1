total_sum = 10

solutions = []

for x in range(total_sum + 1):
    for y in range(total_sum + 1 - x):
        z = total_sum - x - y
        solutions.append((x, y, z))


for solution in solutions:
    print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")