import sys

xs, ys = [], []
with open(sys.argv[1]) as file:
    for line in file:
        x, y = line.split()
        xs.append(int(x))
        ys.append(int(y))
xs.sort()
ys.sort()
total_distance = 0
for x, y in zip(xs, ys):
    distance = abs(x - y)
    total_distance += distance
print(total_distance)
