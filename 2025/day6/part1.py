matrix = []
operators = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line[0].isdigit():
            row = list(map(int, line.split()))
            matrix.append(row)
        else:
            operators = line.split()
r = len(matrix)
sum=0
for i,op in enumerate(operators):
    if op=='*':
        product=1
        for j in range(0,r):
            product*=matrix[j][i]
        sum+=product
    elif op =="+":
        s=0
        for j in range(0,r):
            s+=matrix[j][i]
        sum+=s
print(sum,)