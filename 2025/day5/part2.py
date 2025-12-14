ranges=[]
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
ranges.sort()
merged = []

for a, b in ranges:
    if not merged or merged[-1][1] < a:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1], b)
count =0
for a,b in merged:
    count+=b-a+1
print(count)
