import bisect
ranges = []
numbers = []
r = True
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            r = False
            continue

        if r:
            a, b = map(int, line.split("-"))
            ranges.append((a,b))
        else:
            numbers.append(int(line))
ranges.sort()
merged = []

for a, b in ranges:
    if not merged or merged[-1][1] < a:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)

ranges = merged
fresh=0

starts = [a for a, b in ranges]

def exists(x):
    i = bisect.bisect_right(starts, x) - 1
    return i >= 0 and x <= ranges[i][1]
for i in numbers:
    if exists(i):
        fresh+=1

print(fresh)