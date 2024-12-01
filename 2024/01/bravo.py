from collections import Counter
import sys

ys_frequency = Counter()
with open(sys.argv[1]) as file:
    for line in file:
        _, y = line.split()
        ys_frequency.update([int(y)])

similarity = 0
with open(sys.argv[1]) as file:
    for line in file:
        x, _ = line.split()
        similarity += int(x) * ys_frequency[int(x)]

print(similarity)
